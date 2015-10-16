__author__ = 'Nicholas'


import sys
class Graph:

    def __init__(self):
        """
        Initialize the variable used in Graph
        """
        self.dfsPaths = [] #list for dfsPaths
        self.VertexList = {} #list for adjacent vertices


    def readInputGraph(self, inputFile):
        """
        Reads specified input file and stores in
        adjacency list
        :param inputFile: file to be rad in
        :return: the VertexList
        """
        file = open(inputFile, 'r') #open the file and read it
        for line in file: #for each element in the file
            (vertex,val) = line.split() #vertex gets first value in the line, val gets second
            if vertex not in self.VertexList: #if vertex not in VertexList
               self.VertexList[vertex] = set([val]) #add adjacent pairs
            else:   #else
                self.VertexList.get(vertex).add(val) #add the values
        return self.VertexList #return list of adjacent vertices

    def dfsSearch(self, graph, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                paths += self.dfsSearch(graph, node, end, path)
            return paths

