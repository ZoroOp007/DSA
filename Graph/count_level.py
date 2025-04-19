from .Graph_python import Graph
 
def count_level(self,root):
        level = { key : -1 for key in self.vertices}
         
        queue = []
        visited = {key : "white" for key in self.vertices}
         
        queue.append(root)
        visited[root] = "grey"
        level[root] = 0 
        
        while( not( len(queue) == 0 )):
            
            v = queue.pop(0)
            
            for neighbours in self.adjacency_list[v]:
                
                if( visited[neighbours] == "white"):
                    queue.append(neighbours)
                    visited[neighbours] = "grey"
                    level[neighbours] = level[v] + 1 
        return level
        
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
    g.display()
    l = g.count_level(2)
    
    print("\n\n",l)