# problem link
# https://leetcode.com/problems/find-in-mountain-array/description/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# Triple Binary search


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l = 0
        n = mountain_arr.length()
        r = n - 1
        while(l < r):
            mid = ( l + r ) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        # print(peak)
        l = 0
        r = peak
        while(l <= r):
            mid = ( l + r ) // 2
            # print(l,r,mid)
            v = mountain_arr.get(mid) 
            if v < target:
                l = mid + 1
            elif v == target:
                return mid 
            else:
                r = mid - 1
        l = peak
        r = n - 1
        while(l <= r):
            mid = ( l + r ) // 2
            v = mountain_arr.get(mid) 
            if v > target:
                l = mid + 1
            elif v == target:
                return mid 
            else:
                r = mid - 1
        return -1