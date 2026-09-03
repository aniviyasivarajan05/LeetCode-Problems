class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # If minimum is odd, all even numbers can subtract mn
        # and become odd.
        if mn % 2 == 1:
            return True

        # If minimum is even, possible only if all are even
        for num in nums1:
            if num % 2 == 1:
                return False

        return True