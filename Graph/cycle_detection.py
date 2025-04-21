"""
Cycle detection problem is common question in Graph
here we will use dfs in order to check for any cycle in the undirected graph

Intution : if there is any back edge present then a cycle is found

Back edge : any edge to the parent of a vertex

BackTrack ke sam
"""

from Graph_python import Graph

parent = {}
visited = {}

def cycle_detection(G):

    for vertex in G.vertices:
        visited[vertex] = "white"
        parent[vertex] = -1


    for vertex in G.vertices:

        if visited[vertex] == "white":
            cycle_detection_visit(G,vertex)


def cycle_detection_visit(G,v):

    visited[v] = "grey"

    for neighbour in G.adjacency_list[v]:

        if visited[neighbour] == "white":
            parent[neighbour] = v
            cycle_detection_visit(G,neighbour)

        if visited[neighbour] == "grey" and not(neighbour == parent[v]):
            print("cycle")

    visited[v] = "black"


if __name__ == "__main__":

    g = Graph()

    g.add_edge(5,6)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(3,5)
    g.add_edge(3,6)

    cycle_detection(g)
