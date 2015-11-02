"""
__author__ = 'Nicholas'
__author__ = 'Trent'
"""


from Vertex import *
import sys

class GraphDriver:
    def __init__(self):
        self.graph = Graph()

def main():
    graph = Graph()
    inFile = sys.argv[1]
    d = graph.readInputGraph(inFile)
    #d = graph.readf(inFile)

    userInput = input("Enter a source and destination:")

    dog = userInput.split(" ", -1)


    for path in graph.dfsSearch(d, dog[0], dog[1]):
        print(path)

    cycle = graph.cycle_exists(d)
    print(cycle)


    # disconnected graph without a cycle





if __name__ == '__main__':
    main()