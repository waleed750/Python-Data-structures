"""
     u
    / \
   v - x - w
insert_vertext - vertex_count - vertices
edges - edges_count - get_edge - insert_edge
degree - incident edges (outgoin = True)
inceindent edges if the flight g comes from or to airport v 

"""


class Graph:
    class Vertex:
        __slots__ = "_element"

        def __init__(self, e):
            self._element = e

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge:
        def __init__(self, v, u, x=None):
            self._origin = v
            self._destination = u
            self._element = x

        def endpoints(self):
            """return tuple of origin and destination"""
            return (self._origin, self._destination)

        def opposite(self, v):
            return v if self._origin else self._destination

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    def is_directed(self):
        return self._incoming is not self._outgoing
    def insert_vertex(self,x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed() :
            self._incoming[v] = {}
        return v
    def vertices(self):
        return self._outgoing.keys()
    def vertex_count(self):
        return len(self._outgoing)
    #! vertex end 
    def insert_edge(self,v,u,x = None):
        e = self.Edge(v,u,x)
        self._outgoing[v][u] = e
        self._outgoing[u][v] = e
    def edges(self):
        s = set()
        for secondary_map in self._outgoing.values():
            s.update(secondary_map.values())
        return s 
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total  if self.is_directed else total // 2
    def get_edge(self,v,u):
        return self._outgoing[v].get(u)
    def degree(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    #! Assignment 10.1
    def remove_vertex(self, u):
        if u not in self._outgoing:
            raise KeyError(f"Vertex {u} not found in the graph")

        # Delete outgoing edges from v to other vertices
        for vertex in self._outgoing[u]:
            if self.is_directed():
                del self._incoming[vertex][u]  # Delete incoming edge
            del self._outgoing[vertex][u]  # Delete opposite edge

        # Delete v from _outgoing and _incoming
        del self._outgoing[u]
        if self.is_directed():
            del self._incoming[u]
    #! Assignment 10.2
    def remove_edge(self,e):
        #remove first in outgoing map 
        for vertex , edges in self._outgoing.items():
            for d , edge in edges.items():
                if e is edge:
                   v , u = vertex , d
        del self._outgoing[v][u]
        del self._outgoing[u][v] 
        if self.is_directed():
            del self._incoming[v][u]
            del self._incoming[u][v] 

    def print_all_outgoing_edges(self):
        for vertex, edges in self._outgoing.items():
            print(f"Vertex {vertex.element()}:")
            for destination, edge in edges.items():
                print(f"  -> {destination.element()} (Edge: {edge.element()})")
def DFS(g,u,visited):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in visited: # v is an unvisited vertex
           visited[v] = e # e is the tree edge that visited v
           DFS(g, v, visited) # recursively explore from v

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

# for u in g.vertices():
#     for v in g.vertices():
#         if g.get_edge(u,v) != None:
#             print('Edge (', u.element() ,',', v.element(),') is:',g.get_edge(u,v).element())

g.print_all_outgoing_edges()

# g.remove_vertex(u)
edge_w_z = g.get_edge(w,v)
g.remove_edge(edge_w_z)
print("\nAfter deleting: ")
g.print_all_outgoing_edges()

#!_______DFS_______
visited = { u: None }
DFS(g,z,visited)
for v in visited:
    print(v.element() , end=" ")
