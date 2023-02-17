# problem link
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

# brute force -  linked list

# recursion
# O(N) , O(N)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper( n, k):
            if(n==1):
                return 0
            return (helper(n-1,k) + k) % n
        return helper(n,k)+1   #+1 is for converting 0-based indexing to 1-based indexing


# Optimal
# O(N) , O(1)
# recursion to iterative

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(1,n+1):
            ans = (ans + k) % i
        return ans +1   #+1 is for converting 0-based indexing to 1-based indexing