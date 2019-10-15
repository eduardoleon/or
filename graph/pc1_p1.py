from graph import Graph

graph = Graph(7, 1000, True)
graph[0, 1] = 4
graph[0, 2] = 9
graph[0, 3] = 5
graph[1, 2] = 1
graph[1, 4] = 7
graph[2, 3] = 2
graph[2, 4] = 5
graph[2, 5] = 4
graph[3, 5] = 5
graph[4, 5] = 1
graph[4, 6] = 6
graph[5, 6] = 8
path = graph.shortest_path(0, 6)
print(path)
