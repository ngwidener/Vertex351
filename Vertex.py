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
        self.dfsPaths = []  # list for dfsPaths
        self.VertexList = {}  # list for adjacent vertices
        self.graph = {}


    def readInputGraph(self, inputFile):
        """
        Reads specified input file and stores in
        adjacency list
        :param inputFile: file to be rad in
        :return: the VertexList
        """
        file = open(inputFile, 'r')  # open the file and read it
        for line in file:  # for each element in the file
            (vertex, val) = line.split()  # vertex gets first value in the line, val gets second
            if vertex not in self.VertexList:  # if vertex not in VertexList
                self.VertexList[vertex] = set([val])  #add adjacent pairs
            else:  # else
                self.VertexList.get(vertex).add(val)  #add the values

        for i in list(self.VertexList.keys()):  # for each element in the list of the vertex keys
            for j in self.VertexList[i]:  # for each vertex that's in i
                if j not in self.VertexList:  # if j is not in the vertex list
                    self.VertexList[j] = set()  #we add it to the vertex list

        return self.VertexList  # return list of adjacent vertices



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
            return [path]  # return the list of paths
        if start not in graph:  # if the start element is not in the graph
            print('Not Found')  # prints out not found
            return []  # return an empty list
        paths = []  # path list
        for node in graph[start]:  # for node in the graph

            if node not in path:  # if not in the path
                newpaths = self.dfsSearch(graph, node, end, path)  #new paths we found

                for newpath in newpaths:  #for each new path in the list of new paths
                    paths.append(newpath)  #add the new path to our list of paths

        paths.sort()  # sort our paths

        return paths  # return our paths


    def cycle_exists(self, G):  # - G is a directed graph
        color = {u: "white" for u in G}  # - All nodes are initially white
        found_cycle = [False]  # - Define found_cycle as a list so we can change
        # its value per reference, see:

        for u in G:  # - Visit all nodes.
            if color[u] == "white":
                self.dfs_visit(G, u, color, found_cycle)
            if found_cycle[0]:
                break
        return found_cycle[0]

    def dfs_visit(self, G, u, color, found_cycle):
        if found_cycle[0]:  # - Stop dfs if cycle is found.
            return
        color[u] = "gray"  # - Gray nodes are in the current path
        for v in G[u]:  # - Check neighbors, where G[u] is the adjacency list of u.
            if color[v] == "gray":  # - Case where a loop in the current path is present.
                found_cycle[0] = True
                return
            if color[v] == "white":  # - Call dfs_visit recursively.
                self.dfs_visit(G, v, color, found_cycle)
        color[u] = "black"  # - Mark node as done.


    """
    def readf(self, infile):
        d = {}
        with open(infile, 'r') as f:
            for line in f:
                (key, val) = line.split()
                if key in d:
                    d[key].append(val)
                else:
                    d[key] = [val]
        for x, v in d.items():
            return x, v


    def find_path(self, g, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not g.has_key(start):
            return []
        paths = []
        for node in g[start]:
            if node not in path:
                newpaths = self.find_path(g, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    """