class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            
            # Shrink the window until s[right]'s frequency is <= 2
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len