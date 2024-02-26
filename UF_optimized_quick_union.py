# Weighted quick-union with path compression
# WQUPC
class QuickUnionUF:
    
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1]*N
    
    def get_root(self, elem):
        while(elem != self.id[elem]):
            self.id[elem] = self.id[self.id[elem]]         # PATH COMPRESSION OPTIONAL FOR MORE EFFECIANCY
            elem = self.id[elem]
        return elem

    def is_connected(self, elem1, elem2):
        return self.get_root(elem1) == self.get_root(elem2)

    def union(self, elem1, elem2):
        elem1_root = self.get_root(elem1)
        elem2_root = self.get_root(elem2)
        if elem1 == elem2:
            return
        if self.sz[elem1_root] < self.sz[elem2_root]:
            self.id[elem1_root] = elem2_root
            self.sz[elem1_root] += self.sz[elem2_root]
        else:
            self.id[elem2_root] = elem1_root
            self.sz[elem2_root] += self.sz[elem1_root]

