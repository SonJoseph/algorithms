'''
Input: src = 0, V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [3, 2, 2], [3, 4, 10], [0,3,1]] 

Get shortest path from source to all other nodes.

(0) -4- (1) -6- (4)
|  \           /
8    1      3
|      \   /
(2) -2- (3)

{
    0:0
    1:4
    2:3 
    3:1
    4:4
}


0: 0
1: 4
2: 8
3: 1
4: 4

Keep a dictionary D of distances from the start node to all other nodes.
0: 0
1: inf
2: inf
3: inf
4: inf

Keep a min-heap H of (node_to_visit, distance_to_source)

min-heap = [(0, 0)]

Algorithm:
   1. pop element X off H.
   2. visit neighbors Y and Z of X. 
   3. update distance to neighbor if E[X, Y] + D[X] < D[Y]
'''
from collections import defaultdict 
import heapq

src = 0 
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [3, 2, 2], [3, 4, 3], [0,3,1]]  

def get_shortest_paths(src: int, edges: list[list[int]]):
    graph  = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    distances = {node: float('inf') for node in graph.keys()}
    distances[src] = 0
    min_heap = [(0, src)] # process node with least distance to it first.

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)

        # we have already discovered a path which is shorter
        if curr_dist > distances[curr_node]:
            continue

        for nei, w in graph[curr_node]:
            dist_to_nei = curr_dist + w
            if dist_to_nei < distances[nei]:
                heapq.heappush(min_heap, (dist_to_nei, nei))
                distances[nei] = dist_to_nei

    return distances
        



# def get_shortest_paths(edges: list[list[int]], src: int):
#     graph = defaultdict(list) # {node: [(neighbor, weight)]}

#     '''
#     0: [(1, 4), (2, 8)]
#     1: [(0, 4), (4, 6)]
#     '''
#     for edge in edges:
#         graph[edge[0]].append((edge[1], edge[2]))
#         graph[edge[1]].append((edge[0], edge[2]))

    
#     distances = {node: float('inf') for node in graph.keys()}
#     distances[src] = 0

#     min_heap = []
#     heapq.heappush(min_heap, (0, src))

#     while min_heap:
#         curr_dist, curr_node = heapq.heappop(min_heap)

#         '''
#         find example where this is true.

#         (0) 
#         |  \         
#         8    1      
#         |      \   
#         (2) -2- (3)

#         d = {0: 0, 2: inf, 3: inf}
#         pop (0, 0)
#             d = {0: 0, 2: 8, 3: 1}
#             push (1, 3), (8, 2)
#         pop (1, 3)
#             update d[2] = 3 since E[3, 2] + d[3] (2 + 1) < d[2] (8)
#             d = {0: 0, 2: 3, 3: 1}
#             push (3, 2)
#         pop (3, 2)
#             don't push (11, 0) and (3, 3) since d[0]=0 and d[3] = 1. 
#                 if new_dist < dist[nei] <- prevents us from visiting cycles.
#         pop (8, 2)
#             d[2] = 3 so skip it.
#                  if current_distance > distances[curr_node] <- prevents us from visiting old edges.
#         '''
#         print(f"visiting node {curr_node} with distance {curr_dist}")
        
#         if curr_dist > distances[curr_node]:
#             print(f" skipping node since current shortest distance is {curr_dist}")
#             continue

#         for nei, dist in graph[curr_node]:
#             new_dist = dist + curr_dist
#             if new_dist < distances[nei]:
#                 print(f" adding node {nei} since new distance {new_dist} is less than the current shortest distance {distances[nei]}")
#                 distances[nei] = new_dist
#                 heapq.heappush(min_heap, (new_dist, nei)) 
#             else:
#                 print(f" not adding node {nei} since new distance {new_dist} is greater than the current shortest distance {distances[nei]}")


#     return distances
    
d = get_shortest_paths(src, edges)

print(d)

    

