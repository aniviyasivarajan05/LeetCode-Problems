class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # If we have more than k ones, move left
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # We have exactly k ones
            if ones == k:
                # Remove leading zeros to make the substring as short as possible
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                # Update if shorter or lexicographically smaller
                if (best == "" or
                    len(current) < len(best) or
                    (len(current) == len(best) and current < best)):
                    best = current

        return best
        