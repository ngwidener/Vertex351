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
    #d = graph.readGraph(inFile)
    #print(d)
    #m = graph.getLists(inFile)
    #print(m)

    f = graph.matrix(inFile)



    userInput = input("Enter a source and destination:")

    dog = userInput.split(" ", -1)

    print("[DFS paths]:")
    for path in graph.dfsSearch(d, dog[0], dog[1]):
        print(path)
    print("\n")

    print("[Cycle]:")
    cycle = graph.cycle_exists(d)
    if (cycle == True):
        print("Cycle exists")
    elif (cycle == False):
        print("No cycle exists")
    print("\n")

    #m = graph.readMatrix(inFile)
    #print(m)

    print("[TC]:")
    graph.warshall(f)


    #graph.warshall(d)





    # disconnected graph without a cycle





if __name__ == '__main__':
    main()