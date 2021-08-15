class QuickUnion:
    def __init__(self, vertices):
        self.DisjointOrderedDictForQuickFind = dict()
        for v in vertices:
            self.DisjointOrderedDictForQuickFind[v] = v
        print(self.DisjointOrderedDictForQuickFind)

    def find(self, vertex):
        root = self.DisjointOrderedDictForQuickFind[vertex]
        while self.DisjointOrderedDictForQuickFind[root] != root:
            root = self.DisjointOrderedDictForQuickFind[root]
        return root

    def union(self, vertex_x, vertex_y):
        rootX = self.find(vertex_x)
        rootY = self.find(vertex_y)
        if rootX != rootY:
            self.DisjointOrderedDictForQuickFind[rootY] = rootX
        print(
            "After Union of {}, {} set looks like {}".format(vertex_x, vertex_y, self.DisjointOrderedDictForQuickFind))

    def connected(self, vertex_x, vertex_y):
        return self.find(vertex_x) == self.find(vertex_y)


if __name__ == '__main__':
    vertices = [chr(i) for i in range(ord('A'), ord('F'))]
    unf = QuickUnion(vertices)
    unf.union('A', 'B')
    unf.union('B', 'C')
    unf.union('C', 'D')
    print(unf.connected('C', 'E'))
