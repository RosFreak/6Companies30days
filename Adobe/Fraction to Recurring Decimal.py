#problem link
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/

class Solution:
    # @return a string
    def fractionToDecimal(self, n, d):
        res = ''
        if n == 0:
            return str(n)
        if (n < 0) ^ (d < 0):
            res += '-'
        n = abs(n)
        d = abs(d)
        res += str(n // d)
        if (n % d == 0):
            return res
        res += '.'
        r = n % d
        m = {}
        while r:
            if r in m:
                res = res[:m[r]] + '(' + res[m[r]:] + ')'
                break
            m[r] = len(res)
            r *= 10
            res += str(r // d)
            r %= d
        return res