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

    print("[DFS paths: " + dog[0]+ "," + dog[1] +"]")


    for path in graph.dfsSearch(d, dog[0], dog[1]):
        if dog[0].isdigit() or dog[1].isdigit():

            print(path)

        else:
            print('these are not valid inputs')
            sys.exit(0)

    print("\n")

    print("[Cycle]:")
    cycle = graph.cycle_exists(d)
    if (cycle == True):
        print("Cycle exists")
    elif (cycle == False):
        print("No cycle exists")
    print("\n")


    print("[TC]:")
    graph.warshall(f)
    print("\n")

    #graph.compare()
    #print("[New Edge]:")
    #graph.compareMatrix(d, f)
    graph.compare()



if __name__ == '__main__':
    main()