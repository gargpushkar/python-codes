class Digraph:
    
    def __init__(self, V):
        self.V = V
        self.adj_list = []
        for i in range(V):
            self.adj_list.append([])
    
    def add_edge(self, v, w):
        self.adj_list[v].append(w)
    
    def get_adj(self, v):
        return self.adj_list[v]
    
