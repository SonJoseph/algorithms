from collections import defaultdict, deque
from typing import List

class Solution:
    '''
    [0, 1, 50], [1, 2, 50], [0, 2, 200], k = 0
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        solns = [] # all solns with less than k stops

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        q = deque([(src, 0)]) # (node, cost)
        visited = set([src])

        stops = 0

        while q:
            for _ in range(len(q)):
                # cost accrued on this path
                curr, cost = q.pop()

                print((curr, cost))

                if curr != src and curr != dst:
                    stops += 1

                if curr == dst and stops <= k:
                    print(stops)
                    solns.append(cost)

                for nei, nei_cost in graph[curr]:
                    if nei == dst or nei not in visited:
                        q.append((nei, nei_cost + cost))
                        visited.add(nei)

        if len(solns) == 0:
            return -1

        return min(solns)

s = Solution()
# cheapest flight has more than k stops -> 200
print(s.findCheapestPrice(3, [[0, 1, 50], [1, 2, 50], [0, 2, 200]], 0, 2, 0))
# cheapest flight has less than k stops and longer path -> 100
print(s.findCheapestPrice(3, [[0, 1, 50], [1, 2, 50], [0, 2, 200]], 0, 2, 1))
# no flights to the destination under k stops
print(s.findCheapestPrice(4, [[0, 1, 50], [1, 2, 50], [2, 3, 50], [0, 2, 200]], 0, 3, 0))
