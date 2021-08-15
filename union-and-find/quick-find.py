class QuickFind:
    def __init__(self, vertices):
        self.DisjointOrderedDictForQuickFind = dict()
        for v in vertices:
            self.DisjointOrderedDictForQuickFind[v] = v
        print(self.DisjointOrderedDictForQuickFind)

    def find(self, vertex):
        return self.DisjointOrderedDictForQuickFind[vertex]

    def union(self, vertex_x, vertex_y):
        root_of_x = self.find(vertex_x)
        root_of_y = self.find(vertex_y)
        if root_of_x != root_of_y:
            for root in self.DisjointOrderedDictForQuickFind:
                if self.DisjointOrderedDictForQuickFind[root] == root_of_y:
                    self.DisjointOrderedDictForQuickFind[root] = root_of_x
        print(
            "After Union of {}, {} set looks like {}".format(vertex_x, vertex_y, self.DisjointOrderedDictForQuickFind))

    def connected(self, vertex_x, vertex_y):
        return self.DisjointOrderedDictForQuickFind[vertex_x] == self.DisjointOrderedDictForQuickFind[vertex_y]


if __name__ == '__main__':
    vertices = [chr(i) for i in range(ord('A'), ord('F'))]
    unf = QuickFind(vertices)
    unf.union('A', 'B')
    unf.union('B', 'C')
    unf.union('C', 'D')
    print(unf.connected('C', 'E'))
