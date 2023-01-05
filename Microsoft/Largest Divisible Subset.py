# problem link
# https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        dp = []
        child = []
        mx = 0
        for i in range(n):
            dp.append(1)
            child.append(-1)
        for i in range(n):
            for j in range(i):
                if(nums[i] % nums[j] == 0):
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        child[i] = j
            if dp[i]  > dp[mx]:
                mx = i
        while mx != -1:
            ans.append(nums[mx])
            mx = child[mx]
        return ans[::-1]