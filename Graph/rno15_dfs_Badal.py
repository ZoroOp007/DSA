from Adj_graph import Graph

def DFS(G,s):

    for neighbour in G.vertices[s].neighbours:

        if G.vertices[neighbour].color == "White":
            DFS_Visit(G,neighbour)
        

def DFS_Visit(G,i):

    G.vertices[i].color = "Grey"

    print(i)
    for neighbour in G.vertices[i].neighbours:
        if G.vertices[neighbour].color == "White":

            DFS(G,neighbour)
            
            G.vertices[i].color = "Black"


if __name__ == "__main__":

    G = Graph()

    with open ("rno15_dfs_input_Badal.txt") as fp:
        n = int(fp.readline())

        for i in range(n):

            u , v = fp.readline().strip().split(" ")
            G.add_edge(int(u),int(v))

    DFS(G,2)