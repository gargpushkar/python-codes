# Adjacency List implementation
from collections import deque

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

for i in range(v):
    print(i, g.get_adj(i))


marked = [0]*v
edge_to = [-1]*v
print("DFS")
def dfs(graph, vertex, marked, edge_to):
    marked[vertex] = 1
    for i in graph.get_adj(vertex):
        if not marked[i]:
            print(i)
            edge_to[i] = vertex
            dfs(graph, i, marked, edge_to)

dfs(g, 0, marked, edge_to)


print("BFS")
queue = deque()
marked = [0]*v
edge_to = [-1]*v
def bfs(graph, vertex, marked, edge_to):
    marked[vertex] = 1
    queue.append(vertex)
    while(queue):
        vertex = queue.popleft()
        for i in graph.adj_list[vertex]:
            if not marked[i]:
                print(i)
                queue.append(i)
                marked[i] = 1
                edge_to[i] = vertex

bfs(g, 0, marked, edge_to)
