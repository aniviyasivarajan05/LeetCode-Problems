class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Sort unique values
        sorted_values = sorted(set(arr))

        # Assign ranks
        rank = {}
        for i, value in enumerate(sorted_values, 1):
            rank[value] = i

        # Replace each value with its rank
        return [rank[x] for x in arr]
        