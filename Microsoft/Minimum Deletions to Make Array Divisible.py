#problem link
#https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/description/

import math
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        ans = numsDivide[0]
        for i in numsDivide:
            ans = math.gcd(ans , i)
        nums.sort()
        #print(nums)
        cnt = 0
        for i in nums:
            if ans%i == 0:
                return cnt
            cnt+=1
        return -1