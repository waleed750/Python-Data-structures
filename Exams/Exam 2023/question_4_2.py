from z_Graph import Graph


G = Graph(True) # is directed 

# insert vertex
a = G.insert_vertex('a')
b = G.insert_vertex('b')
c = G.insert_vertex('c')
d = G.insert_vertex('d')
e = G.insert_vertex('e')
f = G.insert_vertex('f')
g = G.insert_vertex('g')
print("is directed : " , G.is_directed())

# insert directed edges 
G.insert_edge(a,b,1)
G.insert_edge(b,c,2)
G.insert_edge(b,d,3)
G.insert_edge(c,e,4)
G.insert_edge(d,e,5)
G.insert_edge(d,f,6)
G.insert_edge(f,e,7)
G.insert_edge(e,g,8)

print("All Vertices : ")
for v in G.vertices():
    print(v.element() , end= ' ')
print("\nAll Edges : ")
for edge in G.edges():
    print(edge.element() , end= ' ')
print("\nAll incideint outgoing edges of b : ")
for e in G.incident_edges(b,True):
    print(e.element() , end= ' ')
visited = {a : None}
def BFS(g:Graph,s,visited):
    level = [s] # first level contains s only 
    while len(level) > 0 :
        next_level = []
        for u in level:
            for e in g.incident_edges(u) : 
                v = e.opposite(u)
                if v not in visited:
                    visited[v] = e 
                    next_level.append(v)
        level = next_level
BFS(G,a,visited)
print("\nbfs : ", )
for v in visited:
    print(v.element() , end= ' ')
print()
def construct_path(u,v,visited):
    path = []
    if v in visited:
        path.append(v)
        walk = v
        while walk is not u:
            e = visited[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
    path.reverse()
    return path
seq = construct_path(a,g,visited)
print("Path : " , end=" ")
for v in seq:
    print(v.element() , end= ' ')