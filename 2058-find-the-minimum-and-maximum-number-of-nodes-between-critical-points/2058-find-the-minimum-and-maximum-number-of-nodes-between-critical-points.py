class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        position = 2

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            # Check if current node is a critical point
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):

                if first == -1:
                    first = position
                else:
                    min_dist = min(min_dist, position - last)

                last = position

            prev = curr
            curr = curr.next
            position += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, last - first]