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


        for i in list(self.VertexList.keys()):

            for j in self.VertexList[i]:
                if j not in self.VertexList:
                    self.VertexList[j] = set()

                    #self.VertexList.update({self.VertexList:j})

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
            print( 'There is no path')
            return [] #return an empty list
        paths = [] #path list
        for node in graph[start]: #for node in the graph

            if node not in path: #if not in the path
                newpaths = self.dfsSearch(graph, node, end, path) #new paths we found

                for newpath in newpaths: #for each new path in the list of new paths
                    paths.append(newpath) #add the new path to our list of paths
                    #self.warshall(graph)
        paths.sort() #sort our paths
        self.cycle_exists(graph)
        #self.warshall(graph)

        return paths #return our paths


    def cycle_exists(self, graph):
        """
        Will determine if there is a cycle
        """
        color = {u : "white" for u in graph}#all nodes are initially white
        found_cycle = [False]#define found_cycle as a list so we can change the value
        #print(graph)
        #print(color)
        for u in graph:#visit all the nodes in the graph

            if color[u] == "white":#if color is white
                self.dfs_visit(graph, u, color, found_cycle)#call dfs_visit
            if found_cycle[0]:#if cycle is found
                break #break
        #print(graph)
        print(color)
        #print(found_cycle)
        return found_cycle[0]#return the value of cycle

    def dfs_visit(self, graph, u, color, found_cycle):
        if found_cycle[0]:#if cycle is found stop dfs and return cycle
            return
        color[u] = "gray"#gray nodes are in the current path
        for v in graph[u]:#check neighbors of visited
            if color[v] == "gray": #if color[v] is gray
                found_cycle[0]#cycle found
                return #return cycle
            if color[v] == "white":#if color[v] is white
                self.dfs_visit(graph, v, color, found_cycle)#call dfs_visit
        color[u] = "black"#color[u] is black



    def warshall(self, a):
        """
        Define the floyd warshall algorithm
        """
        assert(len(row) == len(a) for row in a)
        n = len(a)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    a[i][j] = a[i][j] or (a[i][k] and a[k][j])
        return a

