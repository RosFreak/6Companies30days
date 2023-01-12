#problem link
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/?orderBy=hot

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -1
        max = nums[0]
        n = len(nums)
        for i in range(1,n):
                if(max > nums[i]): # the left value is greater then current value
                    end = i # mark that index with end
                
                else:
                    max = nums[i]
        start = 0
        min = nums[n-1]
        for i in range(n-1,-1,-1):
                if(min < nums[i]): # the left value is greater then current value
                    start = i # mark that index with end
                
                else:
                    min = nums[i]
        
        return end - start + 1