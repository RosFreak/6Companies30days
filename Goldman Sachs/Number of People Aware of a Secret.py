#problem link
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/

class Solution:
    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [1] + [0] * forget
        mod = 10 ** 9 + 7
        share = 0
        for i in range(1, n):
            dp[i % forget] = share = (share + dp[(i - delay) % forget] - dp[i % forget]) % mod
        return sum(dp) % mod

    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [1] + [0] * (n - 1)
        mod = 10 ** 9 + 7
        share = 0
        for i in range(1, n):
            dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % mod
        return sum(dp[-forget:]) % mod