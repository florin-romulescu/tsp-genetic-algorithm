"""
This file contains useful algorithms for graphs.
"""

from . import Node, Edge, Graph

Number = float | int

def dijkstra(node_id:int, graph:Graph) -> list[Number]:
    size = len(list(graph.nodes.keys()))
    distances = [float('inf')] * (size + 1)
    visited = [False] * (size + 1)
    distances[node_id] = 0
    
    for _ in range(1, size+1):
        min_distance = float('inf')
        for u in range(1, size+1):
            if distances[u] < min_distance and not visited[u]:
                min_distance = distances[u]
                min_index = u

        visited[min_index] = True
        
        for y in map(lambda node: node.id, graph.get_neighbours(min_index)):
            cost_y = graph.get_edge_cost(min_index, y)
            if not visited[y] and distances[y] > distances[min_index] + cost_y:
                distances[y] = distances[node_id] + cost_y
                    
    return distances

def construct_distance_matrix(graph:Graph) -> list[list[Number]]:
    size = len(list(graph.nodes.keys()))
    dist_matrix = [[float('inf')] * (size + 1)]
    for i in range(1, size+1):
        dist_matrix.append(dijkstra(i, graph))
    return dist_matrix