class Graph():
    """
    A class representing the Graph data structure.
    
    Class level variables : 
    _____________________
    
    vertices : a list of vertex present in graph
    adj_list : a dictionary which contains a list of all neighbours coressponding a vertex as key
    
    Methods : 
    _______
    
    """
    def __init__(self):
        self.vertices = []
        self.adjacency_list = {}
        
    # add a new vertex if it not exists in list of vertices
    def add_vertex(self,v):
        if v not in self.vertices:
            self.vertices.append(v)
            self.adjacency_list[v] = []
        else:
            print("Vertex already in the list of vertices")
            
    # add a new edge if not exists and add vertex 
    def add_edge(self, u, v):
 
        if u in self.vertices and v in self.vertices:
            
            if u in self.adjacency_list[v] and v in self.adjacency_list[u]:
                pass
            else:
                self.adjacency_list[u].append(v)
                self.adjacency_list[v].append(u)
        else:
            self.add_vertex(u) if u not in self.vertices else self.add_vertex(v)
            self.add_edge(u,v)
            
    def display(self):
        for vertex in self.vertices:
            print(f"{vertex} : {self.adjacency_list[vertex]}")
            
            
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
    