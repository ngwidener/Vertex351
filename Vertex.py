"""
__author__ = 'Nicholas Widener'
__author__ = 'Trent Weatherman'
__version__ = 'October 2015'
Vertex class reads in our graph and
performs a depth first search on it
and performs the transitive closure operation.
Vertex class also checks for cycles in our graph.
"""

import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Initialize the variable used in Graph
        """
        self.dfsPaths = []  # list for dfsPaths
        self.VertexList = {} # list for adjacent vertices
        self.list1 = []
        self.list2 = []
        self.adjMatrix = []
        self.original_adj_matrix = []


    def readInputGraph(self, inputFile):
        """
        Reads specified input file and stores in
        adjacency list
        :param inputFile: file to be rad in
        :return: the VertexList
        """
        file = open(inputFile, 'r')  # open the file and read it
        for line in file:  # for each element in the file
            (vertex, val) = line.split()  #vertex gets first value in the line, val gets second
            if vertex not in self.VertexList:  #if vertex not in VertexList
                self.VertexList[vertex] = {val}  #add adjacent pairs
            else:  #else
                self.VertexList.get(vertex).add(val)  #add the values

        for i in list(self.VertexList.keys()):  # for each element in the list of the vertex keys
            for j in self.VertexList[i]:  # for each vertex that's in i
                if j not in self.VertexList:  #if j is not in the vertex list
                    self.VertexList[j] = {}  #we add it to the vertex list

        return self.VertexList  # return list of adjacent vertices

    def getLists(self, inputFile):
        #list1 = []
        #list2 = []
        #list3 = []

        file = open(inputFile, 'r')
        for line in file:
            pair = line.split()
            self.list1.append(pair[0])
            self.list2.append(pair[1])
        file.close()
        return self.list1, self.list2


    def matrix(self, inputFile):
        self.getLists(inputFile)
        n = 7
        self.adjMatrix = [[0 for v in range(n)] for u in range(n)]

        for i in range(len(self.list1)):
            u = int(self.list1[i])
            v = int(self.list2[i])


            self.adjMatrix[u][v] = 1

        return self.adjMatrix

    def originalMatrix(self, inputFile):
        self.getLists(inputFile)
        n = 7
        self.original_adj_matrix = [[0 for v in range(n)] for u in range(n)]

        for i in range(len(self.list1)):
            u = int(self.list1[i])
            v = int(self.list2[i])


            self.original_adj_matrix[u][v] = 1

        return self.original_adj_matrix

    def printMatrix(self, matrix):
        for i in range(len(matrix)):

            for k in range(len(matrix[0])):

                print(matrix[i][k], " ", end='')
                #print(i, k)
            print('')

    def compare(self):
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix)):
                if self.adjMatrix[i][j] == 1 and self.original_adj_matrix[i][j] == 0:
                    print(i, j)


    def warshall(self, matrix):
        assert (len(row) == len(matrix) for row in matrix)
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

        return  matrix


    def dfsSearch(self, graph, start, end, path=[]):
        """
        Performs a depth first search on
        the graph that is read in from the file
        :param graph: the graph that we are performing the search on
        :param start: the starting vertex
        :param end: the target vertex
        :param path: a list of the paths
        :return: the paths from the search
        """
        path = path + [start]  # path
        if start == end:  # if the start element and end element are the same
            return [path]  #return the list of paths
        if start not in graph:  # if the start element is not in the graph
            print('Not Found')  #prints out not found
            return []  #return an empty list
        paths = []  # path list
        for node in graph[start]:  # for node in the graph

            if node not in path:  #if not in the path
                newpaths = self.dfsSearch(graph, node, end, path)  #new paths we found

                for newpath in newpaths:  #for each new path in the list of new paths
                    paths.append(newpath)  #add the new path to our list of paths

        paths.sort()  # sort our paths

        return paths  # return our paths


    def cycle_exists(self, graph):  # - G is a directed graph
        color = {u: "white" for u in graph}  # - All nodes are initially white
        found_cycle = [False]  # - Define found_cycle as a list so we can change
        # its value per reference, see:

        for u in graph:  # - Visit all nodes.
            if color[u] == "white":
                self.dfs_visit(graph, u, color, found_cycle)
            if found_cycle[0]:
                break
        return found_cycle[0]

    def dfs_visit(self, graph, u, color, found_cycle):
        if found_cycle[0]:  # - Stop dfs if cycle is found.
            # print('cycle exists')
            return
        color[u] = "gray"  # - Gray nodes are in the current path
        for v in graph[u]:  # - Check neighbors, where G[u] is the adjacency list of u.
            if color[v] == "gray":  # - Case where a loop in the current path is present.
                found_cycle[0] = True
                return
            if color[v] == "white":  # - Call dfs_visit recursively.
                self.dfs_visit(graph, v, color, found_cycle)
        color[u] = "black"  # - Mark node as done.

