# problem link
# https://leetcode.com/problems/maximum-matrix-sum/description/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt = 0
        ssum = 0
        mn = matrix[0][0]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                ele = matrix[i][j]
                ssum += abs(ele)
                if ele < 0:
                    cnt = (cnt + 1)%2
                if abs(ele) < abs(mn):
                    mn = ele
        if cnt == 1:
            ssum -= 2*abs(mn)
        return ssum
                