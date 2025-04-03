#Implement the adjacency list using a graph

class Graph():

    def __init__(self):
        self.adj = {}

    def add_vertex(self,v):
        try:
            self.adj.update({v:[]})
        except Exception as e:
            print("Exception : {e}")

    def add_edge(self,u,v):
        if u in self.adj and v in self.adj:

            self.adj[u].append(v)
            self.adj[v].append(u)

    def display(self):
        for key in self.adj:
            print(f"{key} : {self.adj[key]}")

g = Graph()

g.add_vertex(2)
g.add_vertex(6)
g.add_vertex(3)
g.add_vertex(5)

g.add_edge(2,6)
g.add_edge(3,6)
g.add_edge(5,2)

g.display()