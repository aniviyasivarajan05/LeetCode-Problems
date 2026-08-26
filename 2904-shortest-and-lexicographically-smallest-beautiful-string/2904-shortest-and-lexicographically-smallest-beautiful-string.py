class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Store indices of all '1's in string s
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        # If there are fewer than k '1's, no beautiful substring exists
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        ans = ""
        
        # Examine every group of k consecutive '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            # Update best answer if substring is shorter, 
            # or same length but lexicographically smaller
            if len(sub) < min_len:
                min_len = len(sub)
                ans = sub
            elif len(sub) == min_len and sub < ans:
                ans = sub
                
        return ans