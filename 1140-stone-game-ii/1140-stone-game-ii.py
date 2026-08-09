class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # from index i when M is M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # Can take all remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue

                # Current player chooses X
                for X in range(1, 2 * M + 1):
                    next_M = max(M, X)

                    # After taking X piles, opponent starts at i+X
                    opponent = dp[i + X][next_M]

                    # Total remaining stones - opponent's stones
                    dp[i][M] = max(
                        dp[i][M],
                        suffix[i] - opponent
                    )

        return dp[0][1]