from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        n = len(s)
        ans = []

        # Try to match target from left to right
        for i in range(n):
            ch = target[i]

            if freq[ch] > 0:
                ans.append(ch)
                freq[ch] -= 1
            else:
                # Find the smallest available character greater than target[i]
                for j in range(ord(ch) + 1, ord('z') + 1):
                    c = chr(j)

                    if freq[c] > 0:
                        ans.append(c)
                        freq[c] -= 1

                        # Append remaining characters in sorted order
                        for x in sorted(freq.elements()):
                            ans.append(x)

                        return ''.join(ans)

                # Cannot increase at this position
                break

        # Backtrack and try to increase an earlier position
        for i in range(len(ans) - 1, -1, -1):
            # Put the current character back
            freq[ans[i]] += 1

            # Find the smallest character greater than target[i]
            for j in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(j)

                if freq[c] > 0:
                    ans[i] = c
                    freq[c] -= 1

                    # Add remaining characters in sorted order
                    result = ans[:i + 1]

                    for x in sorted(freq.elements()):
                        result.append(x)

                    return ''.join(result)

        return ""
        