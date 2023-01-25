# problem link
# https://leetcode.com/problems/knight-probability-in-chessboard/description/

def isValid(i,j,n):
    if i>=0 and j>=0 and i<n and j<n:
        return True
    return False
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        curr = [[0 for i in range(n)] for i in range(n)]
        next = [[0 for i in range(n)] for i in range(n)]
        curr[row][column] = 1
        for val in range(k):
            for i in range(n):
                for j in range(n):
                    if curr[i][j] != 0:
                        for x in [(-2,-1) , (-1,-2) , (-2,1) , (-1,2) , (1,2) , (2,1) , (2,-1) , (1,-2)]:
                            ni = i+x[0]
                            nj = j+x[1]
                            if isValid(ni, nj , n):
                                next[ni][nj] += curr[i][j] / 8.0
            curr = next
            next = [[0 for i in range(n)] for i in range(n)]
        p = 0
        for i in range(n):
            for j in range(n):
                p += curr[i][j]
        return p
