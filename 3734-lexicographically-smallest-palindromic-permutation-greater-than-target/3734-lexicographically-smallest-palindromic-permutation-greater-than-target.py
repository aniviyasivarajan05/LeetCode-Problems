class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count frequencies
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd-frequency character
        odd_count = 0
        mid = ""

        for i in range(26):
            if freq[i] % 2 == 1:
                odd_count += 1
                mid = chr(ord('a') + i)

        if odd_count > 1:
            return ""

        # Characters available for the first half
        half_count = [x // 2 for x in freq]
        half_len = n // 2

        def build_palindrome(half):
            if n % 2 == 1:
                return half + mid + half[::-1]
            return half + half[::-1]

        # Try to construct the smallest palindrome > target
        def find_answer(pos, counts, prefix):
            if pos == half_len:
                candidate = build_palindrome(prefix)
                return candidate if candidate > target else ""

            target_char = ord(target[pos]) - ord('a')

            # Option 1:
            # Use the same character as target[pos]
            if counts[target_char] > 0:
                counts[target_char] -= 1

                result = find_answer(
                    pos + 1,
                    counts,
                    prefix + target[pos]
                )

                counts[target_char] += 1

                if result:
                    return result

            # Option 2:
            # Use the smallest available character greater than target[pos]
            for c in range(target_char + 1, 26):
                if counts[c] > 0:
                    counts[c] -= 1

                    remaining = []

                    for j in range(26):
                        remaining.append(
                            chr(ord('a') + j) * counts[j]
                        )

                    half = (
                        prefix
                        + chr(ord('a') + c)
                        + "".join(remaining)
                    )

                    counts[c] += 1

                    return build_palindrome(half)

            return ""

        return find_answer(0, half_count, "")