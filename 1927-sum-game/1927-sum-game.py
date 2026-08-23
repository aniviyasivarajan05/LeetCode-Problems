class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        # Calculate initial sums and count '?' in left and right halves
        left_sum = 0
        left_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        right_sum = 0
        right_q = 0
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        # If total question marks difference is odd, Alice always wins
        if (left_q + right_q) % 2 != 0:
            return True
        
        # Bob wins if and only if the difference in digit sums is balanced
        # by the difference in question mark count times 4.5 (or * 9 / 2)
        return (left_sum - right_sum) != (right_q - left_q) * 9 // 2