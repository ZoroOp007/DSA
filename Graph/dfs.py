from Graph_python import Graph

visited = {}

def dfs(G):

    for vertex in G.vertices:
        visited[vertex] = "white"

    for vertex in G.vertices:
        if( visited[vertex] == "white"):
            dfs_visit(G,vertex)

def dfs_visit(G,v):

    print(G.adjacency_list)
    visited[v] = "grey"

    for neighbour in G.adjacency_list[v]:

        if visited[neighbour] == "white":
            dfs_visit(G,neighbour)

    visited[v] = "black"
    print(v)

if __name__ == '__main__':
    g = Graph()

    g.add_edge(2,3)
    g.add_edge(2,5)
    

    dfs(g)