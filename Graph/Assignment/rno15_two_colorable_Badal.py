from Graph.Assignment.Adj_graph import Graph
from Queue_DS import Queue
## Breadth first search : also known as level by level traversal

def two_colourable(G : Graph,s):
    
    q = Queue()

    q.enqueue(s)
    G.vertices[s].color = "Red"

    flag = True
    while(not(q.isEmpty()) and flag):
        
        i = q.dequeue()

        for neighbour in  G.vertices[i].neighbours:

            if G.vertices[neighbour].color == "White":

                if G.vertices[i].color == "Red":
                    G.vertices[neighbour].color = "Blue"
                elif G.vertices[i].color == "Blue":
                    G.vertices[neighbour].color = "Red"
            
                q.enqueue(neighbour)
            else:

                if( G.vertices[neighbour].color == G.vertices[i].color):
                    print(f"{neighbour} and {i} does not fulfill required condition")
                    flag = False

    if(flag):
        print("Two colorability satisfied !!!")

                    
                


if __name__ == "__main__":
    
    G = Graph()

    with open ("rno15_bfs_input_Badal.txt") as fp:
        n = int(fp.readline())

        for i in range(n):
            u , v = fp.readline().strip().split(" ")
            
            G.add_edge(int(u),int(v))
    

    two_colourable(G,2)