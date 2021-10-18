#Author - munish7771
# Breadth-first search (BFS) is an algorithm for searching a tree data structure
# for a node that satisfies a given property. It starts at the tree root and explores 
# all nodes at the present depth prior to moving on to the nodes at the next depth level. 
# Extra memory, usually a queue, is needed to keep track of the child nodes that were 
# encountered but not yet explored. 

from collections import defaultdict 

class Graph: 

    def __init__(self): 

        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 

        visited = [False] * (len(self.graph)) 

        queue = [] 

        queue.append(s) 
        visited[s] = True
  
        while queue: 

            s = queue.pop(0) 
            print(s)

            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal starting from vertex 2") 
g.BFS(3)