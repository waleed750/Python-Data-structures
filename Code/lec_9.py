class Graph:
    #------------------------------ nested Vertex class ------------------------------
    class Vertex:
        slots = '_element'
        def __init__(self,x):
            self._element = x
        def element(self):
            return self._element
        def __hash__(self):
            return hash(id(self))
    #------------------------------ nested Vertex class ------------------------------
    class Edge:
        slots = '_origin','_destination','_element'
        def __init__(self,u,v,x):
            self._origin = u
            self._destination = v
            self._element = x
        def endpoints(self):
            return (self._origin, self._destination)
        def opposite(self,v):
            return self._destination if v is self._origin else self._origin
        def element(self):
            return self._element
        def __hash__(self):
            return hash((self._origin, self._destination))
    def __init__(self,directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    def is_directed(self):
        return self._incoming is not self._outgoing
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    def degree(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    def insert_vertex(self,x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    def insert_edge(self,u,v,x=None):
        e = self.Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e

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
print('*'*20)
print('Edge (u,v) is: ',g.get_edge(u,v).element())
print('No. of Edges: ',g.edge_count())
print('No. of Vertices: ',g.vertex_count())
print('The vertices are: ',end='')
for vertex in g.vertices():
    print(vertex.element(),end='')
print()
print('All edges are: ',end='')
for vertex in g.edges():
    print(vertex.element(),end=' ')
print()

for u in g.vertices():
    for v in g.vertices():
        if g.get_edge(u,v) != None:
            print('Edge (', u.element() ,',', v.element(),') is:',g.get_edge(u,v).element())
