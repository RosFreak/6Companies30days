#problem link
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s):
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in range(len(s)):
            count[s[j]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                count[s[i]] -= 1
                i += 1
            res += i
        return res