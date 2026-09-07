class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[j] = number of ways to form t[:j] from processed part of s
        dp = [0] * (n + 1)

        # Empty string t can always be formed in 1 way
        dp[0] = 1

        for i in range(1, m + 1):
            # Traverse backwards so that dp[j-1] is
            # still from the previous iteration
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
        