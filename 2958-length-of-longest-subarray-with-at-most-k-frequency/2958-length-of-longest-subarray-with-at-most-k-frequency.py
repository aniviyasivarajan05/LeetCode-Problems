class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            val = nums[right]
            freq[val] = freq.get(val, 0) + 1
            
            # Shrink window until frequency condition is satisfied
            while freq[val] > k:
                freq[nums[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length
        