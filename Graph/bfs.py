from .Graph_python import Graph

def bfs(self,root):
        queue = []
        visited = {}
        
        for vertex in self.vertices:
            visited[vertex] = "white"
        
        print("BFS Traversal :: ",end=" ")
        queue.append(root)
        
        while(not(len(queue) == 0)):
            
            v = queue.pop(0)
            
            visited[v] = "grey"
            
            for neighbour in self.adjacency_list[v]:
            
                if(visited[neighbour] == "white"):
                    queue.append(neighbour)
                    visited[neighbour] = "grey"
            
            print(v,end=" ")
            visited[v] = "black"


if __name__ == "__main__":
    g = Graph()
    
    g.add_edge(2,3)
    g.add_edge(3,6)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(4,7)
    g.add_edge(2,3)
    g.add_edge(2,3)
    g.add_edge(6,7)
    g.add_edge(7,8)
    
    g.bfs(2)