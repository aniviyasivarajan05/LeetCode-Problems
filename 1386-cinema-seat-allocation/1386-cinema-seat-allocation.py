class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        ans = 2 * n

        for mask in rows.values():
            left  = mask & 0b000000111100   # seats 2-5
            mid   = mask & 0b000011110000   # seats 4-7
            right = mask & 0b001111000000   # seats 6-9

            if left == 0 and right == 0:
                continue          # 2 groups possible
            elif left == 0 or mid == 0 or right == 0:
                ans -= 1           # 1 group possible
            else:
                ans -= 2           # no group possible

        return ans
        