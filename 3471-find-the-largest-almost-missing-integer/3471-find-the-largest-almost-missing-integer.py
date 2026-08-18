class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        ans = -1

        for x in range(51):
            positions = [i for i in range(n) if nums[i] == x]

            windows = set()

            for p in positions:
                start = max(0, p - k + 1)
                end = min(p, n - k)

                for s in range(start, end + 1):
                    windows.add(s)

            if len(windows) == 1:
                ans = x

        return ans