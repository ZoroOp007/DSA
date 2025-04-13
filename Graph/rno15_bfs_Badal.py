from Adj_graph import Graph
from Queue_DS import Queue
## Breadth first search : also known as level by level traversal

def BFS(G : Graph,s):
    
    q = Queue()

    q.enqueue(s)
    G.vertices[s].color = "Grey"

    while(not(q.isEmpty())):
        
        i = q.dequeue()

        print(i)

        G.vertices[i].color == "Black"

        for neighbour in  G.vertices[i].neighbours:

            if G.vertices[neighbour].color == "White":

                q.enqueue(neighbour)
                G.vertices[neighbour].color = "Grey"


if __name__ == "__main__":
    
    G = Graph()

    with open ("rno15_bfs_input_Badal.txt") as fp:
        n = int(fp.readline())

        for i in range(n):
            u , v = fp.readline().strip().split(" ")
            
            G.add_edge(int(u),int(v))

    BFS(G,2)