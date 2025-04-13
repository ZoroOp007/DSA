"""
Adjacency Graph : a graph implementation where all vertices are stored in a list and
                each vertex has list of vertices it is connected to.

Connected : All vertex are reachable from any vertex.

Disconnected Graph : All vertex are not reachable from each vertex.
"""

class Vertex():

    """
    Constructor for class Vertex

    self.value -> stores data inside a vertex
    self.neighbours -> stores neighbour and their corresponding weight of visit.
    self.color -> to check if visited or not
    """
    def __init__(self , val ):

        self.value = val
        self.neighbours = []      
        self.color = "White"
        self.start_time = 0
        self.finish_time = 0


class Graph():

    ## Graph constructor
    def __init__(self):

        self.vertices = {}

    ## Function to add a new vertex in graph
    def add_vertex(self,val):

        node = Vertex(val)

        # if(self.root == None):
        #     self.root = node
        
        self.vertices[val] = node

    
    ## Function to add edge in a graph
    def add_edge(self, u , v,  weight = 0):

        if (u in self.vertices) and (v in self.vertices):

            self.vertices[u].neighbours.append(v)
            self.vertices[v].neighbours.append(u)

        else:
            
            if( not(u in self.vertices) and not(v in self.vertices)):
                self.add_vertex(u)
                self.add_vertex(v)
                self.add_edge(u,v)

            elif( u in self.vertices):
                self.add_vertex(v)
                self.add_edge(u,v)

            else:
                self.add_vertex(u)
                self.add_edge(v,u)

    ## function delelte a vertex of graph
    def del_vertex(self,val):
        for vertex in self.vertices[val].neighbours:
            self.vertices[vertex].neighbours.remove(val)

        self.vertices.pop(val)

    ## function to delete a edge of graph
    def del_edge(self,u,v):
        
        self.vertices[u].neighbours.remove(v)
        self.vertices[v].neighbours.remove(u)

    ## function to print graph
    def print_graph(self):
        for val in self.vertices:
            print(f"{val} : {self.vertices[val].neighbours}")




## Driver Function 
if __name__ == "__main__":

    G = Graph()

    with open ("file1.txt") as fp:
        n = int(fp.readline())

        for i in range(n):
            u , v = fp.readline().strip().split(" ")
            
            G.add_edge(int(u),int(v))

    G.print_graph()