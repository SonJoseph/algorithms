from typing import List
'''
Any live cell with fewer than two live neighbors dies as if caused by under-population.
2 -> was 1 but now 0
Any live cell with two or three live neighbors lives on to the next generation.
3 -> was 1 and now 1
Any live cell with more than three live neighbors dies, as if by over-population.
4 -> was 1 but now 0
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
5 -> was 0 but now 1

2 pass
1. transform data from 0 or 1 to 2 through 5
2. convert 2 through 5 to 0 or 1
'''
class Solution:

    def getLiveNeighbors(self, board, i, j) -> None:
        liveOptions = set([1, 2, 3, 4])

        m = len(board)
        n = len(board[0])

        directions = [ 
            (-1, -1), (-1, 0), (-1, 1), (0, -1), 
            (0, 1), (1, -1), (1, 0), (1, 1)
            ]
        live_ct = 0
        for di, dj in directions:
            i_new, j_new = i + di, j + dj
            if -1 < i_new < m and -1 < j_new < n:
                live_ct += (board[i_new][j_new] in liveOptions)


        print(f"{live_ct} for position {i} and {j}")

        return live_ct


    def updateCell(self, board, i, j) -> None:
        '''
        Any live cell with fewer than two live neighbors dies as if caused by under-population.
2 -> was 1 but now 0
Any live cell with two or three live neighbors lives on to the next generation.
3 -> was 1 and now 1
Any live cell with more than three live neighbors dies, as if by over-population.
4 -> was 1 but now 0
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
5 -> was 0 but now 1
'''
        live_ct = self.getLiveNeighbors(board, i, j)

        if board[i][j] == 1:
            if live_ct < 2:
                board[i][j] = 2
            elif live_ct == 2 or live_ct == 3:
                    board[i][j] = 3
            elif live_ct > 3:
                board[i][j] = 4
        else:
            if live_ct == 3:
                board[i][j] = 5
        

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = {
            0: 0, # 0 stays at 0 unless it turns into 5
            2: 0,
            3: 1,
            4: 0,
            5: 1
        }

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                self.updateCell(board, i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = d[board[i][j]] 

s = Solution()

'''
Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2 -> was 1 but now 0
Any live cell with two or three live neighbors lives on to the next generation.
    3 -> was 1 and now 1
Any live cell with more than three live neighbors dies, as if by over-population.
    4 -> was 1 but now 0
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    5 -> was 0 but now 1
'''

# Testing that updates are made simultaenously.

# case 2 to case 3: (0, 0) -> 0, but (1, 1) -> 1
board = [[1, 0, 0],[0, 1, 1], [0, 0, 0]]

s.gameOfLife(board)

print(board)

# case 4 to case 5: (1, 1) -> 0, but (2, 2) -> 1
board = [[1, 0, 1],[0, 1, 1], [0, 1, 0]]

s.gameOfLife(board)

print(board)