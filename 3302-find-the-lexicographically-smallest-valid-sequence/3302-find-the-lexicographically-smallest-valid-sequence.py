from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        n = len(word1)
        m = len(word2)

        # last[j] = position in word1 where word2[j]
        # can be matched while preserving order
        last = [-1] * m

        j = m - 1

        # Build last[] from right to left
        for i in range(n - 1, -1, -1):

            if j >= 0 and word1[i] == word2[j]:

                last[j] = i

                j -= 1

        # Result
        res = []

        # j = current position in word2
        j = 0

        # 0 = mismatch not used
        # 1 = mismatch already used
        skip = 0

        # Scan word1 from left to right
        for i, c in enumerate(word1):

            # We already selected all characters
            if j == m:
                break

            # Case 1: exact match
            exact_match = (c == word2[j])

            # Case 2: use our one mismatch
            can_use_mismatch = (
                skip == 0
                and
                (
                    j == m - 1
                    or
                    i < last[j + 1]
                )
            )

            if exact_match or can_use_mismatch:

                # If characters are different,
                # this uses our one mismatch
                if c != word2[j]:
                    skip = 1

                # Select this index
                res.append(i)

                # Move to next character of word2
                j += 1

        # We need exactly m selected indices
        if j == m:
            return res

        return []