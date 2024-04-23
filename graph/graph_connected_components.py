# Adjacency List implementation

class Graph:
    
    def __init__(self, V):
        self.V = V
        self.adj_list = []
        for i in range(V):
            self.adj_list.append([])
    
    def add_edge(self, a, b):
        self.adj_list[a].append(b)
        self.adj_list[b].append(a)
    
    def get_adj(self, a):
        return self.adj_list[a]
    

v = 13
e = 13

g = Graph(v)
g.add_edge(0, 5)
g.add_edge(4, 3)
g.add_edge(0, 1)
g.add_edge(9, 12)
g.add_edge(6, 4)
g.add_edge(5, 4)
g.add_edge(0, 2)
g.add_edge(11, 12)
g.add_edge(9, 10)
g.add_edge(0, 6)
g.add_edge(7, 8)
g.add_edge(9, 11)
g.add_edge(5, 3)

# for i in range(v):
#     print(i, g.get_adj(i))


visited = [0]*v

def dfs(graph, vertex, visited):
    visited[vertex] = 1
    for i in graph.get_adj(vertex):
        if not visited[i]:
            dfs(graph, i, visited)

count = 0
for i in range(v):
    if not visited[i]:
        dfs(g, i, visited)
        count +=1
print(count)
