class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Difference in number of '?' between the two halves
        q_diff = left_q - right_q

        # Difference in known digit sums
        sum_diff = left_sum - right_sum

        # Alice wins if the imbalance cannot be neutralized
        if q_diff == 0:
            return sum_diff != 0

        # Alice can force a win when the number of ? differs
        # unless the sum difference is exactly what the remaining
        # '?' can compensate for.
        if abs(q_diff) % 2 == 1:
            return True

        # Maximum compensation possible by the side with more '?'
        if q_diff > 0:
            return sum_diff + (q_diff // 2) * 9 != 0
        else:
            return sum_diff - (abs(q_diff) // 2) * 9 != 0