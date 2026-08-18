class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        
        count = [0] * 51
        
        # Check every subarray of size k
        for i in range(n - k + 1):
            seen = set()
            
            for j in range(i, i + k):
                seen.add(nums[j])
            
            for x in seen:
                count[x] += 1
        
        # Find largest integer appearing in exactly one subarray
        for x in range(50, -1, -1):
            if count[x] == 1:
                return x
        
        return -1
        