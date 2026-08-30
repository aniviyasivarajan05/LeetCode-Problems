class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Remove both from the front
        option1 = right + 1

        # Remove both from the back
        option2 = n - left

        # Remove one from the front and one from the back
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)
        