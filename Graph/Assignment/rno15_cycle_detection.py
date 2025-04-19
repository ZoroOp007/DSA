from Graph.Assignment.Adj_graph import Graph

def DFS(G,s,flag=False):

    for neighbour in G.vertices[s].neighbours:

        if G.vertices[neighbour].color == "White":
            flag = DFS_Visit(G,neighbour)
    return flag
        
    

def DFS_Visit(G,i):

    G.vertices[i].color = "Grey"

    for neighbour in G.vertices[i].neighbours:
        if G.vertices[neighbour].color == "White":

            DFS(G,neighbour)
            
            G.vertices[i].color = "Black"
        
        if G.vertices[neighbour].color == "Grey":
            flag = True
            return flag


if __name__ == "__main__":

    G = Graph()

    with open ("rno15_dfs_input_Badal.txt") as fp:
        n = int(fp.readline())

        for i in range(n):

            u , v = fp.readline().strip().split(" ")
            G.add_edge(int(u),int(v))

    if(DFS(G,2)):
        print("Cycle Detected !!!")
    else:
        print("No Cycle Found !!!")