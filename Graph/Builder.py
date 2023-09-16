# Graph Builder

class Graph:
    def __init__(self):
        self.graph = dict()

    def builder(self, directed):
        num_nodes = int(input('Enter Number of Nodes: '))
        for i in range(1, num_nodes + 1):
            self.graph[i] = set()
        num_edges = int(input('Enter Number of Edges(for directed graph enter exact edges else only num of conn): '))
        for _ in range(num_edges):
            node, edge = map(int, input().split(' '))
            self.graph[node].add(edge)
            if not directed:
                self.graph[edge].add(node)

    def print_graph(self):
        print(self.graph)


obj = Graph()
directed = int(input('For directed enter 1 else 0: '))
obj.builder(directed)
obj.print_graph()
