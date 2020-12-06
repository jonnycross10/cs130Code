from collections import defaultdict 
  
# Class to represent a graph 
  
  
class Graph: 
    def __init__(self, vertices): 
        self.graph = defaultdict(list)  # dictionary containing adjacency List 
        self.V = vertices  # No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self, v, visited, stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack) 
  
        # Push current vertex to stack which stores result 
        stack.append(v) 
  
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack = [] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack) 
  
        # Print contents of the stack 
        print (stack[::-1])  # return list in reverse order 
  
# Driver Code 
#Graph(num) where num is number of nodes
g = Graph(10)

g.addEdge(0,6)
g.addEdge(0,4)
g.addEdge(0,7)
g.addEdge(0,5)

g.addEdge(3,1)
g.addEdge(3,6)
g.addEdge(3,2)
g.addEdge(3,5)

g.addEdge(4,1)
g.addEdge(4,2)
g.addEdge(4,5)

g.addEdge(5,1)

g.addEdge(7,4)
g.addEdge(7,5)
g.addEdge(7,1)
g.addEdge(7,6)
g.addEdge(7,9)
g.addEdge(7,3)

g.addEdge(8,5)
g.addEdge(8,6)
g.addEdge(8,2)

g.addEdge(9,5)
g.addEdge(9,1)
g.addEdge(9,2)
g.addEdge(9,3)



'''
g.addEdge(0,4)
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(0,3)

g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(4,2)

g.addEdge(5,1)
g.addEdge(5,4)
g.addEdge(5,3)
g.addEdge(5,8)
g.addEdge(5,9)

g.addEdge(6,3)
g.addEdge(6,2)
g.addEdge(6,1)
g.addEdge(6,9)

g.addEdge(7,2)
g.addEdge(7,1)

g.addEdge(8,2)
g.addEdge(8,1)
g.addEdge(8,4)
g.addEdge(8,6)

g.addEdge(9,3)
g.addEdge(9,1)
g.addEdge(9,4)
'''

print ("Following is a Topological Sort of the given graph")
  
# Function Call 
g.topologicalSort() 
