"""
__author__ = 'Nicholas'
__author__ = 'Trent'
"""


from Vertex import *
import sys
import numbers

class GraphDriver:
    def __init__(self):
        self.graph = Graph()

def main():
    graph = Graph()
    inFile = sys.argv[1]
    d = graph.readInputGraph(inFile)


    f = graph.matrix(inFile)

    graph.originalMatrix(inFile)

    userInput = input("Enter a source and destination:")

    usr = userInput.split(" ", -1)

    print("[DFS paths: " + usr[0]+ "," + usr[1] +"]")


    for path in graph.dfsSearch(d, usr[0], usr[1]):
        if usr[0].isalpha() or usr[1].isalpha():

            print('these are not valid inputs')
            sys.exit(0)

        else:
            print(path)

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
    graph.compare()
    print("\n")

    #graph.compare()
    #print("[New Edge]:")
    #graph.compareMatrix(d, f)



if __name__ == '__main__':
    main()