# problem link
# https://leetcode.com/problems/magical-string/description/

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = collections.deque([2])
        S = [1,2,2]
        while len(S) < n:
            k = queue.popleft()
            tmp = 3 - S[-1]
            # print(tmp,S[-1],k)
            for i in range(k):
                S.append(tmp)
                queue.append(tmp)
        return S[:n].count(1)