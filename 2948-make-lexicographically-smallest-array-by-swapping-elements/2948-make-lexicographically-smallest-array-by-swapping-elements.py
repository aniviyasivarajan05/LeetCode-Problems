class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))
        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find all elements in the same swappable group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Get and sort only the indices
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted because arr is sorted
            for i, idx in enumerate(indices):
                ans[idx] = arr[start + i][0]

            start = end + 1

        return ans