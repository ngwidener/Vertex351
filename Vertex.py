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


        for i in list(self.VertexList.keys()): #for each element in the list of the vertex keys
            for j in self.VertexList[i]: # for each vertex that's in i
                if j not in self.VertexList: #if j is not in the vertex list
                    self.VertexList[j] = set() #we add it to the vertex list

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
            print( 'Not Found')#prints out not found
            return [] #return an empty list
        paths = [] #path list
        for node in graph[start]: #for node in the graph

            if node not in path: #if not in the path
                newpaths = self.dfsSearch(graph, node, end, path) #new paths we found

                for newpath in newpaths: #for each new path in the list of new paths
                    paths.append(newpath) #add the new path to our list of paths

        paths.sort() #sort our paths


        return paths #return our paths


    def cycle_exists(self, graph): # -graph is our graph.
        color = { node : "white" for node in graph}  #color all nodes white to begin with
        found_cycle = False # found_cycle set to false

        for node in graph: # for each node in graph.
            if color[node]:#if the color[node] is white
                self.dfs_visit(graph, node, color, found_cycle) #we call the dfs_visit method
            if found_cycle:#if a cycle is found
                found_cycle = True
                break#break
        return found_cycle #return the true or false

    def dfs_visit(self,graph, node, color, found_cycle):
        if found_cycle: # if a cycle is found return to the cycle_exists method
            return
        color[node] = "gray"#else color the node gray
        for neighbor in graph[node]: #for every neighbor in the graph of the node
            if color[neighbor] == "gray": #If neighbor is gray
                found_cycle = True # then a cycle exists.
                return
            if color[neighbor] == "white": #if the neighbor is white
                self.dfs_visit(graph, neighbor, color, found_cycle)# call dfs_visit .

        color[node] = "black"# color the original node black

