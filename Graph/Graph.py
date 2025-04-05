#first we try to  implement the graph with matrix

class Matrix_Graph():
    def __init__(self, v):
        self.matrix = [[0]*v for _ in range(v)]

    def print_matrix(self):
        print(self.matrix)
    
    def add_edge(self, u,v):
        try:
            if(self.matrix[u][v] == 0):
                self.matrix[u][v] = 1
                self.matrix[v][u] = 1

                print("New edge added successfully!")
            else:
                print("Edge Aready defined")
        except Exception as e:
            print(f"Oops! an exception raised : {e}")
    
    def delete_edge(self, u, v):
        try:
            if(self.matrix[u][v] == 1):
                self.matrix[u][v] = 0
                self.matrix[v][u] = 0

                print("Edge deleted successfully!")
            else:
                print("No such edge is present")
        except IndexError as e:
            print(f"Oops! an exception raised : {e}")
            

## Graph Implementation using adjacency list




## Note : This is the implementation of UNDIRECTED GRAPH
class Graph():
    
    def __init__(self):
        self.adj = {}

    def add_vertex(self,val):
        self.adj[val] = []

    def add_edge(self,u,v):
        if(u not in self.adj):
            self.adj[u] = []
        
        if(v not in self.adj):
            self.adj[v] = []
        
        self.adj[u].append(v)
        self.adj[v].append(u)

    def print_graph(self):
        pass

if __name__ == "__main__":

    g = Graph()

    g.add_vertex(2)
    g.add_vertex(12)
    g.add_vertex(25)
    g.add_vertex(26)

    g.add_edge(2,12)
    g.print_graph()
        