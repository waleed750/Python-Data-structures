class Graph:
    class Vertex:
        __slots__ = '_element'
        def __init__(self,x=None):
            self._element = x
        def element(self):
            return self._element
        def __hash__(self):
            return hash( id (self))
    class Edge:
        __slots__ = '_element' , '_origin' , '_destination'
        def __init__(self,u,v,x=None):
            self._origin = u 
            self._element = x 
            self._destination = v
        def endpoints(self):
            '''return tuple of origin and destination'''
            return (self._origin , self._destination)
        def opposite(self,e):
            return self._origin if e is self._origin else self._destination
        def element(self):
            return self._element
        def __hash__(self) :
            return hash( (self._origin , self._destination) )
    def __init__(self,directed=False):
        '''in case of directed Graph and undirected Graph '''
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    def is_directed(self):
        return self._incoming is not self._outgoing
    #! vertex functions 
    def insert_vertex(self,x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    #! Edges Functions 
    def insert_edge(self,u,v,x=None):
        edge = self.Edge(u,v,x)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values() :
            result.update(secondary_map.values())
        return result
    def edges_count(self):
        total = sum(len(self._outgoing[v] for v in self._outgoing))
        return total if self.is_directed() else total // 2
    def get_edge(self,u,v):
        return self._outgoing[u].get(v)
    #!degrees(v) retrun number of edges- retrun edges incident_edges(v) edges that comes in or out from the vertex
    def degree(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    #! Assignment 
    def remove_vertex(self,u):
        vertex_temp = u.element()
        if u not in self._outgoing:
            raise KeyError("Key Error "+ repr(vertex_temp))
        for v , edges in self._outgoing.items():
            # we will need the current vertex
            if u in edges:
                del self._outgoing[v][u]
                if self.is_directed() : del self._incoming[v][u] 
            
        #! at the end remove the key 'u' from outgoing and incoming 
        del self._outgoing[u]
        if self.is_directed():
            del self._incoming[u]
        return vertex_temp
    def print_graph(self,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for v , edges in adj.items():
            print(f"Vertex : {v.element()}")
            for destination , edge in edges.items():
                print(f"    ->  ({destination.element()}) = {edge.element()}")

g = Graph()
u = g.insert_vertex('u')
v = g.insert_vertex('v')
w = g.insert_vertex('w')
z = g.insert_vertex('z')
g.insert_edge(u,v,'e')
g.insert_edge(u,w,'g')
g.insert_edge(v,w,'f')
g.insert_edge(w,z,'h')
print('Degree of vertex u: ', g.degree(u,False))
print('Degree of vertex v: ', g.degree(v,False))
print('Degree of vertex w: ', g.degree(w,False))
print('Degree of vertex z: ', g.degree(z,False))
print('Is directed? ',g.is_directed())
print('All (outging) edges incident to u: ',end='')
for edge in g.incident_edges(u):
    print(edge.element(), end=' ')
print()
print('All (outging) edges incident to v: ',end='')
for edge in g.incident_edges(v):
    print(edge.element(), end=' ')
print()
print('All (outging) edges incident to w: ',end='')
for edge in g.incident_edges(w):
    print(edge.element(), end=' ')
print()
print('All (outging) edges incident to z: ',end='')
for edge in g.incident_edges(z):
    print(edge.element(), end=' ')
g.print_graph()
print("\nBefore deleting vertex v")
g.remove_vertex(v)
print("\nAfter deleting vertex v")
g.print_graph()