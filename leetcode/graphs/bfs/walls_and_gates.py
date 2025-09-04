'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
'''
from collections import deque

def findDistanceToNearestGate(grid: list[list[int]]) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])
    q = deque([])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                q.append((i, j, 0))

    # BFS will converge when no dist < grid[nei_i][nei_j] or we have explored all empty rooms
    while q:
        i, j, dist = q.popleft()

        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nei_i, nei_j = i + di, j + dj
            if m > nei_i > -1 and n > nei_j > -1 and grid[nei_i][nei_j] != -1 and grid[nei_i][nei_j] != 0:
                # a shorter distance from a gate to this position was found, we need to potentially update it's neighbors.
                if dist + 1 < grid[nei_i][nei_j]:
                    grid[nei_i][nei_j] = dist + 1
                    q.append((nei_i, nei_j, dist + 1))

    return grid

print(findDistanceToNearestGate([[-1, -1, -1, 2147483647], [-1, 2147483647, 2147483647, -1],[0, 2147483647, 2147483647, 0]]))

    

