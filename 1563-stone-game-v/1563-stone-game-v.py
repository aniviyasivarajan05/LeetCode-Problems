class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # Prefix sum array for dynamic range sum lookups
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] = max(dp[i][k] + get_sum(i, k)) for k in range(i, j + 1)
        # max_right[i][j] = max(dp[k][j] + get_sum(k, j)) for k in range(i, j + 1)
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0  # Mid pointer for splitting index
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Advance 'mid' pointer where left_sum <= right_sum
                mid = max(i, mid)
                while mid < j and get_sum(i, mid) * 2 <= get_sum(i, j):
                    mid += 1
                
                # mid is now the first index where left_sum > right_sum
                
                best = 0
                
                # Case 1: left_sum < right_sum (k ranges from i to mid - 2)
                if mid - 1 >= i:
                    if get_sum(i, mid - 1) * 2 == get_sum(i, j):
                        # Exact equal split at mid - 1
                        best = max(best, max_left[i][mid - 1])
                        best = max(best, max_right[mid][j])
                        if mid - 2 >= i:
                            best = max(best, max_left[i][mid - 2])
                    else:
                        best = max(best, max_left[i][mid - 1])
                        
                # Case 2: left_sum > right_sum (k ranges from mid to j - 1)
                if mid < j:
                    best = max(best, max_right[mid + 1][j])
                
                dp[i][j] = best
                max_left[i][j] = max(max_left[i][j - 1], best + get_sum(i, j))
                max_right[i][j] = max(max_right[i + 1][j], best + get_sum(i, j))

        return dp[0][n - 1]
        