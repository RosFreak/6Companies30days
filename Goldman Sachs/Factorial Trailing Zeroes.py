# problem link
#https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        d = int(n/5)
        while d!=0:
            ans += d
            d = int(d/5)
        return ans