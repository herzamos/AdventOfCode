import sys
from queue import PriorityQueue

def dijkstra(start_vertex, edges, weights, end):
    D = {(i, j):float('inf') for (i, j) in edges.keys()}
    D[start_vertex] = 0
    visited = set()

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)

        for neighbor in edges[current_vertex]:
            distance = weights[neighbor]
            if neighbor not in visited:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D[end]
        
def adjacentIndices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def partOne():
    with open("15.txt", "r") as f:
        m = [list(map(int, list(x.strip()))) for x in f.readlines()]
    m[0][0] = 0
    edges = {}
    weights = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            edges[(i, j)] = adjacentIndices(i, j, len(m), len(m[0]))
            weights[(i, j)] = m[i][j]
    print(dijkstra((0,0), edges, weights, (len(m) - 1, len(m[0]) - 1)))
    
def partTwo():
    with open("15.txt", "r") as f:
        m = [list(map(int, list(x.strip()))) for x in f.readlines()]
    new_m = [[0 for i in range(len(m[0] * 5))] for j in range(len(m) * 5)]
    for i in range(len(new_m)):
        for j in range(len(new_m[0])):
            new_m[i][j] = (m[i % len(m)][j % len(m[0])] + i // len(m) + j // len(m[0])) % 10 + (m[i % len(m)][j % len(m[0])] + i // len(m) + j // len(m[0])) // 10
    new_m[0][0] = 0
    edges = {}
    weights = {}
    for i in range(len(new_m)):
        for j in range(len(new_m[0])):
            edges[(i, j)] = adjacentIndices(i, j, len(new_m), len(new_m[0]))
            weights[(i, j)] = new_m[i][j]
    print(dijkstra((0,0), edges, weights, (len(new_m) - 1, len(new_m[0]) - 1)))

partTwo()