class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from pile i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones the current player
        # can collect starting from index i with current M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Process from the end towards the beginning
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # If we can take all remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue

                # Try taking X piles
                best = 0

                for X in range(1, 2 * M + 1):
                    # Stones taken now
                    taken = suffix[i] - suffix[i + X]

                    # Opponent gets the best possible result
                    opponent = dp[i + X][max(M, X)]

                    # Current player wants to maximize their stones
                    best = max(best, taken + suffix[i + X] - opponent)

                dp[i][M] = best

        return dp[0][1]
        