class Solution:
    def longestSubsequence(self, nums):
        total = 0

        for x in nums:
            total ^= x

        if total != 0:
            return len(nums)

        for x in nums:
            if x != 0:
                return len(nums) - 1

        return 0
        