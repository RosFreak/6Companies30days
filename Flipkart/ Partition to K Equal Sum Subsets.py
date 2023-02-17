# problem link
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
# https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
# not complete yet

def solve(setno , ind , nums , sumlist , k):
    if ind == len(nums):
        if setno == k:
            flag = 1
            for i in range(1,k):
                if sumlist[i] != sumlist[i-1]:
                    flag = 0
                    break
            if flag:
                return True
        return False
    for i in range(k):
        if sumlist[i] > 0:
            sumlist[i] += nums[ind]
            v = solve(setno , ind + 1 , nums , sumlist , k)
            if v:
                return True
            sumlist[i] -= nums[ind]
        else:
            sumlist[i] += nums[ind]
            v = solve(setno + 1 , ind + 1 , nums , sumlist , k)
            if v:
                return True
            sumlist[i] -= nums[ind]
    return False
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        s = sum(nums)
        if s % k != 0 or k > len(nums):
            return False
        sumlist = [0 for i in range(k)]
        setno = 0
        ind = 0
        return solve(setno , ind , nums , sumlist , k)

# other approach same issue
def solve(visited , ind , nums , totsum , cursum , n, k):
    if k == 0:
        return True
    if cursum > totsum:
        return False
    if cursum == totsum:
        return solve(visited , 0 , nums , totsum , 0 , n, k-1)
    for i in range(ind,n):
        if visited[i]:
            continue
        visited[i] = True
        if solve(visited , ind+1 , nums , totsum ,cursum + nums[i], n, k):
            return True
        visited[i] = False
    return False
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        s = sum(nums)
        n = len(nums)
        if s % k != 0 or k > len(nums):
            return False
        totsum = s/k
        visited = [False for i in nums]
        ind = 0
        return solve(visited , ind , nums , totsum , 0 , n, k)