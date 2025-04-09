# l = [1,3,2,5,6,87,3]

# if( 2,3 in l):
#     print(True)
# else:
#     print(False)

# a =5
# print( a if( a> 5) else 12)

# vertex = []
# edges = []

# def add_edge(u,v):
#     edges.append((u,v))

# add_edge(2,3)
# print(edges)

# for edge in edges:
#     if( 2 in edge):
#         print(edge)

d = {1:[2,3],2:[1,3,4,5],4:[2,3,1]}

for key in d:
    print(f"Vertex : {key} is connected with vertices : {d[key]}")
