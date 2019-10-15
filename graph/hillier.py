from graph import Graph

def prob_10_3_2():
    graph = Graph(7, 1000, True)
    graph[0, 1] = 40
    graph[0, 2] = 60
    graph[0, 3] = 50
    graph[1, 2] = 10
    graph[1, 4] = 70
    graph[2, 3] = 20
    graph[2, 4] = 55
    graph[2, 5] = 40
    graph[3, 5] = 50
    graph[4, 5] = 10
    graph[4, 6] = 60
    graph[5, 6] = 80
    return graph

def prob_10_3_3():
    graph = Graph(4, 1000, False)
    graph[0, 1] = 8
    graph[0, 2] = 18
    graph[0, 3] = 31
    graph[1, 2] = 10
    graph[1, 3] = 21
    graph[2, 3] = 12
    return graph

def prob_10_3_4_a():
    graph = Graph(7, 1000, True)
    graph[0, 1] = 4
    graph[0, 2] = 6
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
    return graph

def prob_10_3_4_b():
    graph = Graph(11, 1000, True)
    graph[0, 1] = 4
    graph[0, 2] = 3
    graph[0, 3] = 6
    graph[1, 3] = 5
    graph[1, 4] = 3
    graph[2, 3] = 4
    graph[2, 5] = 6
    graph[3, 4] = 2
    graph[3, 5] = 5
    graph[3, 6] = 2
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
    return graph

def prob_10_3_6():
    graph = Graph(8, 1000, False)
    graph[0, 1] = 4.6
    graph[0, 2] = 4.7
    graph[0, 3] = 4.2
    graph[1, 4] = 3.5
    graph[1, 5] = 3.4
    graph[2, 4] = 3.6
    graph[2, 5] = 3.2
    graph[2, 6] = 3.3
    graph[3, 5] = 3.5
    graph[3, 6] = 3.4
    graph[4, 7] = 3.4
    graph[5, 7] = 3.6
    graph[6, 7] = 3.8
    return graph

def prob_10_4_2():
    graph = Graph(8, 1000, True)
    graph[0, 1] = 1.3
    graph[0, 2] = 2.1
    graph[0, 3] = 0.9
    graph[0, 4] = 0.7
    graph[0, 5] = 1.8
    graph[0, 6] = 2.0
    graph[0, 7] = 1.5
    graph[1, 2] = 0.9
    graph[1, 3] = 1.8
    graph[1, 4] = 1.2
    graph[1, 5] = 2.6
    graph[1, 6] = 2.3
    graph[1, 7] = 1.1
    graph[2, 3] = 2.6
    graph[2, 4] = 1.7
    graph[2, 5] = 2.5
    graph[2, 6] = 1.9
    graph[2, 7] = 1.0
    graph[3, 4] = 0.7
    graph[3, 5] = 1.6
    graph[3, 6] = 1.5
    graph[3, 7] = 0.9
    graph[4, 5] = 0.9
    graph[4, 6] = 1.1
    graph[4, 7] = 0.8
    graph[5, 6] = 0.6
    graph[5, 7] = 1.0
    graph[6, 7] = 0.5
    return graph

def prob_10_4_3():
    graph = Graph(6, 10000, True)
    graph[0, 1] = 190
    graph[0, 2] = 70
    graph[0, 3] = 115
    graph[0, 4] = 270
    graph[0, 5] = 160
    graph[1, 2] = 100
    graph[1, 3] = 110
    graph[1, 4] = 215
    graph[1, 5] = 50
    graph[2, 3] = 140
    graph[2, 4] = 120
    graph[2, 5] = 220
    graph[3, 4] = 175
    graph[3, 5] = 80
    graph[4, 5] = 310
    return graph
