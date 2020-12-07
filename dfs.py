
# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
 
# Driver code
 
 
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 2)
g.addEdge(0, 9)
g.addEdge(0, 4)

g.addEdge(1,9)
g.addEdge(1,7)
g.addEdge(1,4)
g.addEdge(1,2)

g.addEdge(2,6)
g.addEdge(2,9)
g.addEdge(2,1)
g.addEdge(2,0)


g.addEdge(3,8)
g.addEdge(3,6)
g.addEdge(3,5)
g.addEdge(3,7)
g.addEdge(3,4)

g.addEdge(4,8)
g.addEdge(4,3)
g.addEdge(4,1)
g.addEdge(4,0)

g.addEdge(5,8)
g.addEdge(5,6)
g.addEdge(5,3)

g.addEdge(6,9)
g.addEdge(6,8)
g.addEdge(6,5)
g.addEdge(6,3)
g.addEdge(6,2)

g.addEdge(7,9)
g.addEdge(7,3)
g.addEdge(7,1)

g.addEdge(8,6)
g.addEdge(8,5)
g.addEdge(8,4)
g.addEdge(8,3)

g.addEdge(9,7)
g.addEdge(9,6)
g.addEdge(9,2)
g.addEdge(9,1)
g.addEdge(9,0)

print("Following is DFS from (starting from vertex 2)")
g.DFS(0)
