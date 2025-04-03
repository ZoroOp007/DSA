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

class Vertex():
    def __init__(self,val):
        self.data = val
        self.neighbour = []


## Note : This is the implementation of UNDIRECTED GRAPH
class Graph():
    
    def __init__(self):
        self.root = None
        self.adj = []

    def add_vertex(self,val):

        v = Vertex(val)

        if(self.root == None):
            self.root = v
            self.adj.append(v)
        else:
            self.adj.append(v)

    def add_edge(self,u,v):
        if( u,v in self.adj):
            for x in self.adj:
                if(u == x.data):
                    x.neighbour.append(v)
        else:
            print(f"Vertex {u} doesn't exists !!!")
    
    def print_graph(self):
        for i in self.adj:
            print(i.data ,": ")
            for j in i.neighbour:
                print(j.data," ")



if __name__ == "__main__":

    g = Graph()

    g.add_vertex(2)
    g.add_vertex(12)
    g.add_vertex(25)
    g.add_vertex(26)

    g.
    g.print_graph()
        