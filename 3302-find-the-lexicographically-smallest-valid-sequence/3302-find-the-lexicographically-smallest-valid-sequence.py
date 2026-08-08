class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # suff[i] stores the max length of word2's suffix matching word1[i:]
        suff = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suff[i] = m - 1 - j

        ans = []
        j = 0
        mismatch_used = False
        
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            else:
                # Try using the single allowed mismatch here
                if not mismatch_used and suff[i + 1] >= m - 1 - j:
                    ans.append(i)
                    j += 1
                    mismatch_used = True
                    
        return ans if len(ans) == m else []