# PROBLEM LINK
#https://leetcode.com/problems/rotate-function/description/

import numpy
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        mx =  numpy.dot( nums, numpy.array([i for i in range(n)]) )
        mx0 = mx
        for i in range(n-1):
            mx0 = mx0 + s - n*nums[n-i-1]
            mx = max(mx , mx0)
        return mx
        