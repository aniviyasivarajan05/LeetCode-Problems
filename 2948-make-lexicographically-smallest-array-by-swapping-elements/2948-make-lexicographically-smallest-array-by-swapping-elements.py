class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((num, i) for i, num in enumerate(nums))

        result = nums[:]
        group = []

        for i in range(n):
            group.append(arr[i])

            if i == n - 1 or arr[i + 1][0] - arr[i][0] > limit:
                indices = sorted(idx for val, idx in group)
                values = sorted(val for val, idx in group)

                for idx, val in zip(indices, values):
                    result[idx] = val

                group = []

        return result 