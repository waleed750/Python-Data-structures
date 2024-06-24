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
            self._incoming = {}
        return v
    def insert_edge(self,u,v,e = None):
        e = self.Edge(u,v,e)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e 
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



def DFS(graph,u,visited):
    for e in graph.incident_edges(u):
        v = e.opposite(u)
        if v not in visited:
            visited[v] = e 
            DFS(graph,v,visited)
def construct_path(u,v,visited):
    path = []
    if v in visited:
        path.append(v)
        walk = v
        while walk is not u :
            e = visited[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
    path.reverse()
    return path
def BFS(graph,s,visited):
    level = [s] # first level contains only s 
    while len(level) > 0 :
        next_level = [] # prepare the next level 
        for u in level:
            for e in graph.incident_edges(u):
                v = e.opposite(u)
                if v not in visited:
                    visited[v] = e 
                    next_level.append(v)
        level = next_level


# G = Graph()
# u = G.insert_vertex('u')
# v = G.insert_vertex('v')
# z = G.insert_vertex('z')
# w = G.insert_vertex('w')
# print("Vertices are : ")
# for v in G.vertices():
#     print(v.element() ,end= " ")
# print()

# g = G.insert_edge(u,w,'g')
# e = G.insert_edge(u,v,'e')
# f = G.insert_edge(v,w,'f')
# h = G.insert_edge(w,z,'h')

# for edge in G.edges():
#     print(edge.element())


# print(f"Degree of v : {}")
# visited = { u: None }
# DFS(G,u,visited)

# for x in visited:
#     print(x.element() , end=" ")
# def BFS(graph : Graph,s,visited):
#     level = [s] # frist level include only s 
#     while len(level) > 0 :
#         next_level = [] # prepare the list of the next level
#         for u in level:
#             for e in graph.incident_edges(u):
#                 v = e.opposite(u)
#                 if v not in visited:
#                     visited[v] = e
#                     next_level.append(v)
#         level = next_level

# BFS(G,v,visited)
# for x in visited:
#     print(x.element() , end=" ")

def main():
    G = Graph()
    # vertices
    v0 = G.insert_vertex('Seattle')
    v1 = G.insert_vertex('San_Francisco')
    v2 = G.insert_vertex('Los_Angeles')
    v3 = G.insert_vertex('Denver')
    v4 = G.insert_vertex('Kansas_City')
    v5 = G.insert_vertex('Chicago')
    v6 = G.insert_vertex('Boston')
    v7 = G.insert_vertex('New_York')
    v8 = G.insert_vertex('Atlanta')
    v9 = G.insert_vertex('Miami')
    v10 = G.insert_vertex('Dallas')
    v11 = G.insert_vertex('Houston')

    # edges
    G.insert_edge(v0, v1)
    G.insert_edge(v0, v3)
    G.insert_edge(v0, v5)
    G.insert_edge(v1, v2)
    G.insert_edge(v1, v3)
    G.insert_edge(v2, v3)
    G.insert_edge(v2, v4)
    G.insert_edge(v2, v10)
    G.insert_edge(v3, v4)
    G.insert_edge(v3, v5)
    G.insert_edge(v4, v5)
    G.insert_edge(v4, v7)
    G.insert_edge(v4, v8)
    G.insert_edge(v4, v10)
    G.insert_edge(v5, v6)
    G.insert_edge(v5, v7)
    G.insert_edge(v6, v7)
    G.insert_edge(v7, v8)
    G.insert_edge(v8, v9)
    G.insert_edge(v8, v10)
    G.insert_edge(v8, v11)
    G.insert_edge(v9, v11)
    G.insert_edge(v10, v11)
    visited1 = {v5 : None}

    # G.remove_vertex(v11)
    # G.remove_vertex(v9)
    
    DFS(G,v5,visited1)
    print(G.vertex_count(), ' vertices are searched in this DFS order:')
    for v in visited1:
        print(v.element(),end=" ")
    print(f"The path from {v5.element()} to {v10.element()} : ")
    path = construct_path(v5,v10,visited1)
    for v in path:
        print(v.element(),end=" ")
        
    visited2 = {v5 : None}
    BFS(G,v5,visited2)
    print(f"vertices searched are searched in BFS order : ",G.vertex_count())
    for v in visited2:
        print(v.element(),end=" ")
    path2 = construct_path(v5,v10,visited2)
    print(f"The path from {v5.element()} to {v10.element()} : ")
    for v in path2:
        print(v.element(),end=" ")

def BFS(graph, s):
    visited = set()
    queue = []
    visited.add(s)
    queue.append(s)
    
    while queue:
        u = queue.pop(0)
        print(f"Visited vertex: {u.element()}")
        
        for e in graph.incident_edges(u):
            v = e.opposite(u)
            if v not in visited:
                visited.add(v)
                queue.append(v)

# if __name__ == "__main__":
#     main()
#! test remove_edge function 
# def main2():
#     G = Graph()
#     # vertices
#     v0 = G.insert_vertex('Seattle')
#     v1 = G.insert_vertex('San_Francisco')
#     v2 = G.insert_vertex('Los_Angeles')
#     v3 = G.insert_vertex('Denver')
#     v4 = G.insert_vertex('Kansas_City')
#     v5 = G.insert_vertex('Chicago')
#     v6 = G.insert_vertex('Boston')
#     v7 = G.insert_vertex('New_York')
#     v8 = G.insert_vertex('Atlanta')
#     v9 = G.insert_vertex('Miami')
#     v10 = G.insert_vertex('Dallas')
#     v11 = G.insert_vertex('Houston')

#      # edges
#     G.insert_edge(v0, v1, 'e0')
#     G.insert_edge(v0, v3, 'e1')
#     G.insert_edge(v0, v5, 'e2')
#     G.insert_edge(v1, v2, 'e3')
#     G.insert_edge(v1, v3, 'e4')
#     G.insert_edge(v2, v3, 'e5')
#     G.insert_edge(v2, v4, 'e6')
#     G.insert_edge(v2, v10, 'e7')
#     G.insert_edge(v3, v4, 'e8')
#     G.insert_edge(v3, v5, 'e9')
#     G.insert_edge(v4, v5, 'e10')
#     G.insert_edge(v4, v7, 'e11')
#     G.insert_edge(v4, v8, 'e12')
#     G.insert_edge(v4, v10, 'e13')
#     G.insert_edge(v5, v6, 'e14')
#     G.insert_edge(v5, v7, 'e15')
#     G.insert_edge(v6, v7, 'e16')
#     G.insert_edge(v7, v8, 'e17')
#     G.insert_edge(v8, v9, 'e18')
#     G.insert_edge(v8, v10, 'e19')
#     G.insert_edge(v8, v11, 'e20')
#     G.insert_edge(v9, v11, 'e21')
#     G.insert_edge(v10, v11, 'e22')
    
#     # Display vertices and edges before removal
#     print("Vertices before removal:")
#     for v in G.vertices():
#         print(v.element(), end=" ")
#     print("\nEdges before removal:")
#     for e in G.edges():
#         print(f"({e.endpoints()[0].element()}, {e.endpoints()[1].element()})", end=" ")
#     print("\n")

#     e10 = G.get_edge(v4,v5)
#     # Remove an edge and display the graph after removal
#     G.remove_edge(e10)
    
#     print("Edges after removal of edge between 'Kansas_City' and 'Chicago':")
#     for e in G.edges():
#         print(f"({e.endpoints()[0].element()}, {e.endpoints()[1].element()})", end=" ")
#     print("\n")

# if __name__ == "__main__":
#     main2()

G = Graph()

v1 = G.insert_vertex(1)
v2 = G.insert_vertex(2)
v3 = G.insert_vertex(3)
v4 = G.insert_vertex(4)
v5 = G.insert_vertex(5)
v6 = G.insert_vertex(6)
v7 = G.insert_vertex(7)
v8 = G.insert_vertex(8)

G.insert_edge(v1,v2)
G.insert_edge(v1,v3)
G.insert_edge(v1,v4)
G.insert_edge(v2,v1)
G.insert_edge(v2,v3)
G.insert_edge(v2,v4)

G.insert_edge(v3,v1)
G.insert_edge(v3,v2)
G.insert_edge(v3,v4)

G.insert_edge(v4,v1)
G.insert_edge(v4,v2)
G.insert_edge(v4,v3)
G.insert_edge(v4,v6)

G.insert_edge(v5,v6)
G.insert_edge(v5,v7)
G.insert_edge(v5,v8)

G.insert_edge(v6,v4)
G.insert_edge(v6,v5)
G.insert_edge(v6,v7)

G.insert_edge(v7,v5)
G.insert_edge(v7,v6)
G.insert_edge(v7,v8)

G.insert_edge(v8,v5)
G.insert_edge(v8,v7)
print("Vertex : ",end=" ")
for v in G.vertices():
    print(v.element() ,end=" ")
print()

# G.display()
visitedDFS = {v1 : None}
DFS(G,v1,visitedDFS)
print("Vertices searched from v1 to v8 : ",G.vertex_count())
for v in visitedDFS:
    print(v.element(), end=" ")
pathDFS = construct_path(v1,v8, visitedDFS)
print(f"Path DFS from {v1.element()} to {v8.element()} : ",)
for v in pathDFS:
    print(v.element(), end=" ")