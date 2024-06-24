from z_Graph import Graph


# Initializing the graph and inserting vertices
G = Graph()

cs15 = G.insert_vertex('CS15')
cs16 = G.insert_vertex('CS16')
cs22 = G.insert_vertex('CS22')
cs31 = G.insert_vertex('CS31')
cs32 = G.insert_vertex('CS32')
cs126 = G.insert_vertex('CS126')
cs127 = G.insert_vertex('CS127')
cs141 = G.insert_vertex('CS141')
cs169 = G.insert_vertex('CS169')

# Inserting edges based on prerequisites
G.insert_edge(cs16, cs15)
G.insert_edge(cs31, cs15)
G.insert_edge(cs32, cs16)
G.insert_edge(cs32, cs31)
G.insert_edge(cs126, cs22)
G.insert_edge(cs126, cs32)
G.insert_edge(cs127, cs16)
G.insert_edge(cs141, cs22)
G.insert_edge(cs141, cs16)
G.insert_edge(cs169, cs32)


# Performing DFS to get the course sequence respecting prerequisites
def DFS(g, u, visited):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in visited:
            visited[v] = e
            DFS(g, v, visited)

visited = {cs15: None}
DFS(G, cs15, visited)

# Displaying the followed order
print("\nThe order of courses to be taken respecting prerequisites:")
for x in visited:
    print(x.element(), end=" ")