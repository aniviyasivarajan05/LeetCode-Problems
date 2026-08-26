class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        # Store positions of all 1s
        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best = ""

        # Consider every group of k consecutive 1s
        for i in range(len(ones) - k + 1):
            first = ones[i]
            last = ones[i + k - 1]

            # Minimum substring containing these k ones
            current = s[first:last + 1]

            if best == "":
                best = current
            elif len(current) < len(best):
                best = current
            elif len(current) == len(best) and current < best:
                best = current

        return best
        