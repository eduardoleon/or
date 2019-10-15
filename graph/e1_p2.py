from graph import Graph

graph = Graph(11, 1000, True)
graph[0, 1] = 4
graph[0, 2] = 6
graph[0, 3] = 3
graph[1, 2] = 5
graph[1, 4] = 3
graph[2, 3] = 4
graph[2, 4] = 2
graph[2, 5] = 4
graph[2, 6] = 2
graph[3, 5] = 6
graph[4, 6] = 2
graph[4, 7] = 4
graph[5, 6] = 1
graph[5, 8] = 2
graph[5, 9] = 5
graph[6, 7] = 2
graph[6, 8] = 5
graph[7, 8] = 2
graph[7, 10] = 7
graph[8, 9] = 3
graph[8, 10] = 8
graph[9, 10] = 4
path = graph.shortest_path(0, 10)
print(path)
