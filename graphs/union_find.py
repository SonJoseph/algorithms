'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
'''

#  dont even need graph.
# n = 4
# edges = [
#     [0, 1],
#     [2, 1],
#     [3, 4]
# ]

# graph = [[] for _ in range(n)]
# '''
#  0 - 1 - 2
#  3 - 4

#  [[1, 2],[0, 2],[1],[4],[3]]
# '''
# for edge in edges:
#     graph[edge[0]].append(edge[1])
#     graph[edge[1]].append(edge[0])

# initialize parents to point to themselves
par = [i for i in range(n)]
# initialize components to be of size 1
size = [1 for _ in range(n)]


# 0, 1
# 2, 1
[1 1 1 3]
[1 3 1 1]

union(0, 1)

def union(n1, n2):
    # connect smaller to larger
    if size[n1] > size[n2]:
        par[n2] = par[n1]
        size[par[n1]] += 1
    else:
        par[n1] = par[n2]
        size[par[n2]] += 1

def find(node):
    # connect n2 to par of n1
    while par[node] != node:
        par[node] = par[par[node]] #path compression
        node = par[node]
    return node

for edge in edges:
    union(edge[0], edge[1])

components = set()
for i in range(n):
    components.add(find(i))

return len(components)

    