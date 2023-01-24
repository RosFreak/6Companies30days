# problem link
# https://leetcode.com/problems/count-nice-pairs-in-an-array/description/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        ans = 0
        for i in range(len(nums)):
            val = nums[i] - int(str(nums[i])[::-1])
            ans = (ans + d[val]) % (10 ** 9 + 7)
            d[val] += 1
        return ans