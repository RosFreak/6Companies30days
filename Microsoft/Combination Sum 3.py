# problem link
# https://leetcode.com/problems/combination-sum-iii/description/

def backtrack( ans , curr , size , currsum , ind  , k , n ):
    if (currsum == n) and (size == k):
        ans.append(curr.copy())
        return
    if (size > k) or (currsum > n):
        return
    for i in range(ind,10):
        curr.append(i)
        currsum += i
        backtrack( ans , curr , size + 1 ,currsum , i+1 , k , n)
        curr.pop()
        currsum -= i
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []
        backtrack( ans , curr , 0 ,0 , 1 , k , n)
        return ans
