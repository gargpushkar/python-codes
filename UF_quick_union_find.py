# Still not optimized

class QuickUnionUF:
    
    def __init__(self, N):
        self.id = list(range(N))
    
    def get_root(self, elem):
        while(elem != self.id[elem]):
            elem = self.id[elem]
        return elem
    
    def is_connected(self, elem1, elem2):
        return self.get_root(elem1) == self.get_root(elem2)

    def union(self, elem1, elem2):
        elem1_root = self.get_root(elem1)
        elem2_root = self.get_root(elem2)
        self.id[elem1_root] = elem2_root
