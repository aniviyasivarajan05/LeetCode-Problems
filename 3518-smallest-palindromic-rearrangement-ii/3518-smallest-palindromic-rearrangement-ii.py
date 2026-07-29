from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        half = {}

        for c in sorted(cnt):
            if cnt[c] & 1:
                mid = c
            half[c] = cnt[c] // 2

        m = sum(half.values())

        def ways(freq):
            total = sum(freq.values())
            ans = 1
            rem = total
            for v in freq.values():
                if v:
                    ans *= comb(rem, v)
                    if ans > k:
                        return k + 1
                    rem -= v
            return ans

        if ways(half) < k:
            return ""

        left = []

        while m:
            for c in sorted(half):
                if half[c] == 0:
                    continue

                half[c] -= 1
                cnts = ways(half)

                if cnts >= k:
                    left.append(c)
                    m -= 1
                    break

                k -= cnts
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]