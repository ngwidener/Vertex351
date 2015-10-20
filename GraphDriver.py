__author__ = 'Nicholas'
__author__ = 'Trent'


from Vertex import *
import sys

class GraphDriver:
    def __init__(self):
        self.graph = Graph()

def main():
    graph = Graph()
    inFile = sys.argv[1]
    d = graph.readInputGraph(inFile)

    userInput = input("Enter a source and destination:")

    dog = userInput.split(" ", -1)


    for path in graph.dfsSearch(d, dog[0], dog[1]):
        print(path)
        #print(graph.cycle_exists(graph))


if __name__ == '__main__':
    main()