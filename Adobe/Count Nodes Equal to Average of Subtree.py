# problem link
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt = [0]
        def solve(n,cnt):
            if n == None:
                return 0,0
            l = solve(n.left,cnt)
            r = solve(n.right,cnt)
            ssum = l[0] + r[0] + n.val
            size = l[1] + r[1] + 1
            if (ssum) // (size) == n.val:
                cnt[0] += 1
            return ssum,size
        solve(root,cnt)
        return cnt[0]