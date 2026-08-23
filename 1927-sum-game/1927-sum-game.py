class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')

        left_q = num[:half].count('?')
        right_q = num[half:].count('?')

        diff = left_sum - right_sum

        # If the number of ? is different
        if left_q != right_q:
            if (left_q - right_q) % 2 != 0:
                return True

            return diff + (left_q - right_q) * 9 // 2 != 0

        # Equal number of ? on both sides
        return diff != 0