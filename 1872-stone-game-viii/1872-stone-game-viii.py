class Solution:

  def stoneGameVIII(self, stones: list[int]) -> int:
    n = len(stones)

    # Compute prefix sums
    pref = [0] * n
    pref[0] = stones[0]
    for i in range(1, n):
      pref[i] = pref[i - 1] + stones[i]

    # max_diff tracks max(pref[j] - dp[j]) for j > i
    # At i = n-1, the only available next prefix is j = n (which corresponds to index n-1 in 0-indexed pref)
    max_diff = pref[n - 1]

    # Iterate backwards from n-2 down to 1 (0-indexed)
    for i in range(n - 2, 0, -1):
      dp_i = max_diff
      max_diff = max(max_diff, pref[i] - dp_i)

    return max_diff