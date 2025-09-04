'''
edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

In a directed acyclic graph, get an ordering of nodes such that for each edge (v1, v2), v1 appears before v2 in the ordering.

5, 2, 3, 4, 0, 1
'''

from collections import defaultdict, deque

# edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

def topo_sort_dfs_iter(edges: list[list[int]]):
    graph = defaultdict(list)
    visited = set()
    nodes = set()
    result = []

    for u, w in edges:
        graph[u].append(w)
        nodes.add(u)
        nodes.add(w)

    for node in nodes:
        if node not in visited:
            '''
            1, 2, 3, 3, 2, 1
                4
            '''
            visit_stack = [node]
            while visit_stack:
                node = visit_stack[-1]

                if node not in visited:
                    for nei in graph[node]:
                        if nei not in visited:
                            visit_stack.append(nei)
                    visited.add(node)
                else:
                    # append the node to the result after we "visit" (inspect all neighbors) it
                    # and process all it's downstream nodes.
                    result.append(visit_stack.pop())
    
    return list(reversed(result))


def topo_sort_dfs_rec(edges: list[list[int]]):

    graph = defaultdict(list)
    nodes = set()
    visited = set()
    result = []

    '''
    dfs(0)
     v = [0]
     stack = [0]
     dfs(1)
      v = [0, 1]
      stack = [0, 1]
      result = [1]
     dfs(2)
      v = [0, 1]
      stack = [0, 1]
      result = [1, 2]
     result = [1, 2, 0]
    '''
    def dfs(node, path):
        if node in path:
            raise RuntimeError("cycle detected")
        '''
        We visited this node in a previous DFS, but does not mean there is a cycle.
        
        0  1
        | /
        2
        '''
        if node in visited:
            return

        path.add(node)
        visited.add(node)

        for nei in graph[node]:
            dfs(nei, path)

        result.append(node)
    
    for u, w in edges:
        graph[u].append(w)
        # us this for updating a set with multiple elements.
        nodes.update([u, w])

    for u in nodes:
        dfs(u, set())


    return list(reversed(result))

        
        
        




    
    

# toplogical sort can only exist for a directed acyclic graph (tree)
def kahns(edges: list[list[int]]):

    graph = defaultdict(list)
    indegrees = defaultdict(int) # count the indegrees
    result = []

    for u, v in edges:
        graph[u].append(v)
        indegrees[v] += 1
        if u not in indegrees:
            indegrees[u] = 0

    q = deque([node for node, ct in indegrees.items() if ct == 0])

    while q:
        curr = q.popleft()
        result.append(curr)

        for nei in graph[curr]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)

    if len(result) != len(indegrees):
        # unable to add a node due to indegrees not being 0.
        raise RuntimeError("graph has a cycle!")

    return result

# 3- 0 - 1
#     2 /

# [3, 0, 2, 1]
# [0, 1, 3, 2]


    return result

# tree
edges = [[0, 2], [1, 2]]
# 0, 1, 2
print(topo_sort_dfs_rec(edges))

# cycle
edges = [[0, 2], [2, 1], [1, 0]]
# print(kahns(edges))

# no edges
edges = []
# []
print(kahns(edges))







# Kahn's algorithm
# def sort(edges: list[list[int]]):
#     graph = defaultdict(list)
#     indegrees = defaultdict(int)

#     for u, v in edges:
#         graph[u].append(v)
#         indegrees[v] += 1
#         # this node has no indegrees
#         if u not in indegrees:
#             indegrees[u] = 0

#     # initalize the queue with nodes that have no indegrees.
#     # node 5 and 4. 
#     q = deque([node for node in indegrees if indegrees[node] == 0])
#     result = []

#     while q:
#         node = q.popleft()
#         result.append(node)

#         '''
#         1 - 2
#         3 /
#         '''
#         for nei in graph[node]:
#             indegrees[nei] -= 1
#             # only add node once we've finished processing existing nodes with 0 indegrees.
#             if indegrees[nei] == 0:
#                 q.append(nei)

#     '''
#     1 -> 2 -> 3
#           \   |
#               4
#     '''
#     if len(result) != len(indegrees):
#         raise RuntimeError("Cycle in graph")

#     return result

#def sort_dfs(edges: list[int]):



# edges = [[0, 1], [1, 2], [2, 0]]
# sort(edges)

# edges = [[0, 1], [1, 2], [3, 2]]
# print(sort(edges))



    