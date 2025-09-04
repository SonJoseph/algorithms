'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
'''
import unittest
from typing import List

def generate(n: int) -> List[List[int]]:
    triangle = []

    for i in range(n): #n=0, row of length 1
        row = [1]*(i+1) 
        row[0], row[-1] = 1, 1
        for j in range(1, len(row)-1): # n = 3, update indices 1
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)


        print(triangle)
        print(i)

        #[[1],[1, 1],[1, 1, 1]]
    
    return triangle


    # if n >= 1:
    #     res.append([1])
    # if n >= 2:
    #     res.append([1, 1])
    # if n >= 3:
    #     while n > 2:
    #         next = [1] * (len(res[-1])+1)
    #         prev = res[-1]
    #         for i in range(1, len(next)-1): # O(n^2) n rows, after n=3, scan O(n-1) elements each time.
    #             # i will and i-1 will always be less than and eq to [0, len(res[-1])]
    #             next[i] = prev[i] + prev[i-1]
    #         res.append(next)
    #         n-=1
    # return res

class TestCache(unittest.TestCase):

    def test_getPascals(self):
        self.assertEqual(generate(3), [[1],[1,1],[1,2,1]])


if __name__ == '__main__':
    unittest.main()