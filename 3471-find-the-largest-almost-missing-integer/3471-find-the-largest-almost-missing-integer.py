class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        count = [0] * 51
        freq = [0] * 51

        # First window
        for i in range(k):
            freq[nums[i]] += 1

        for x in range(51):
            if freq[x] > 0:
                count[x] += 1

        # Slide the window
        for i in range(k, n):
            freq[nums[i - k]] -= 1
            freq[nums[i]] += 1

            # Only count numbers currently present
            for x in range(51):
                if freq[x] > 0:
                    count[x] += 1

        # Largest number appearing in exactly one window
        for x in range(50, -1, -1):
            if count[x] == 1:
                return x

        return -1