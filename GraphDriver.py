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
    graph.startGraph(inFile)


if __name__ == '__main__':
    main()