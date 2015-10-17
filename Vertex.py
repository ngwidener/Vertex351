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
        """
        Performs a depth first search on
        the graph that is read in from the file
        :param graph: the graph that we are performing the search on
        :param start: the starting vertex
        :param end: the target vertex
        :param path: a list of the paths
        :return: the paths from the search
        """
        path = path + [start] #path
        if start == end: #if the start element and end element are the same
            return [path] #return the list of paths
        if start not in graph: #if the start element is not in the graph
            return [] #return an empty list
        paths = [] #path list
        for node in graph[start]: #for node in the graph
            if node not in path: #if not in the path
                newpaths = self.dfsSearch(graph, node, end, path) #new paths we found
                for newpath in newpaths: #for each new path in the list of new paths
                    paths.append(newpath) #add the new path to our list of paths
        paths.sort() #sort our paths
        return paths #return our paths

