class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Store reserved seats row-wise
        rows = {}

        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)

        # Initially, every row can accommodate 2 groups
        # (seats 2-5 and 6-9)
        ans = 2 * n

        for r, reserved in rows.items():
            # Check the three possible blocks
            left = any(s in reserved for s in [2, 3, 4, 5])
            middle = any(s in reserved for s in [4, 5, 6, 7])
            right = any(s in reserved for s in [6, 7, 8, 9])

            # If both outer blocks are free -> 2 groups
            if not left and not right:
                continue

            # Otherwise, at most one group can fit
            if not left or not middle or not right:
                ans -= 1
            else:
                # All three blocks are blocked
                ans -= 2

        return ans

        