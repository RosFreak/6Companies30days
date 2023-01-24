# problem link - hard
# https://leetcode.com/problems/maximum-good-people-based-on-statements/description/

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        ans = 0
        for i in range(1,1<<n):
            flag = True
            for j in range(n):
                if not(i & (1 << j)):
                    continue
                for k in range(n):
                    if (i & (1 << k)) and statements[j][k] == 0:
                        flag = False
                        break
                    elif not(i & (1 << k)) and statements[j][k] == 1:
                        flag = False
                        break
                if flag == False:
                    break
            if flag:
                ans = max(ans , i.bit_count())
        return ans