class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0 = 0
        c1 = 0
        c2 = 0

        # Count 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        idx = 0

        # Place 0s
        for i in range(c0):
            nums[idx] = 0
            idx += 1

        # Place 1s
        for i in range(c1):
            nums[idx] = 1
            idx += 1

        # Place 2s
        for i in range(c2):
            nums[idx] = 2
            idx += 1
        