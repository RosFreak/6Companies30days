# problem link
# https://leetcode.com/problems/number-of-matching-subsequences/description/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        ans = 0
        d[None] = 0
        for i in words:
            d[i[0]].append(i[1:])
        for i in s:
            # print(d)
            for x in d.pop(i,()):
                if len(x) > 0:
                    # print(x)
                    d[x[0]].append(x[1:])
                else:
                    d[None] += 1
        return d[None]