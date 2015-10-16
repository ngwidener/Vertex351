__author__ = 'Nicholas'


from Vertex import *
import sys

class GraphDriver:
    def __init__(self):
        self.graph = Graph()

def main():
    graph = Graph()
    input = sys.argv[1]
    d = graph.readInputGraph(input)

    for path in graph.dfsSearch(d, "0", "3"):
        print(path)


if __name__ == '__main__':
    main()