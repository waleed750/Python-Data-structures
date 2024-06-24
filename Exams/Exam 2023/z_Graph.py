class Graph:
    class Vertex:
        __slots__ = '_element'
        def __init__(self , e) -> None:
            self._element = e
        def element(self):
            return self._element
        def __hash__(self):
            return hash(id(self._element))
    class Edge:
        __slots__= '_element' , '_origin' , '_destination'
        def __init__(self,u,v,e) -> None:
            self._element= e 
            self._origin = u
            self._destination = v 
        def endpoints(self):
            return (self._origin,self._destination)
        def opposite(self,v):
            return self._origin if v is self._destination else self._destination
        def element(self):
            return self._element
        def __hash__(self) :
            return hash((self._origin,self._destination))
    def __init__(self,is_directed=False) :
        self._outgoing = {}
        self._incoming = {} if is_directed else self._outgoing
    def len(self):
        return len(self._outgoing)
    def is_directed(self):
        return self._incoming is not self._outgoing
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    def edges_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        raise total if self.is_directed else total // 2
    def get_edge(self,u,v):
        return self._outgoing[u].get(v)
    # inserts 
    def insert_vertex(self,e = None):
        v = self.Vertex(e)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    def insert_edge(self,u,v,x = None):
        e = self.Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e 
    def incident_edges(self,v,outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        for e in adj[v].values():
            yield e 
    def degree(self,v,outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    # def display(self):
    #     for v in self.vertices():
    #         print(f"Vertex : {v.element()}")
    #         for e in self.incident_edges(v):
    #             print(f"\t-> {e._destination.element()} , {e.element()}")
    def remove_vertex(self, v):
        if v not in self._outgoing:
            raise KeyError("Vertex not found " + repr(v))

        # Remove all incident edges first
        for edge in list(self.incident_edges(v)):
            u = edge.opposite(v)
            del self._outgoing[u][v]
            if self.is_directed():
                del self._incoming[v][u]

        # Finally, remove the vertex
        del self._outgoing[v]
        if self.is_directed():
            del self._incoming[v]

    def remove_edge(self, e):
        u , v = e.endpoints()
        del self._outgoing[u][v]
        if self.is_directed():
            del self._incoming[v][u]
        else:
            del self._outgoing[v][u]
