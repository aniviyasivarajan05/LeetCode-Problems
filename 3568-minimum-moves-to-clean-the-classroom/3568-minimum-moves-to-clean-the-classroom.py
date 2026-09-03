from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = []
        litter_id = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = len(litter)
                    litter.append((i, j))

        k = len(litter)

        if k == 0:
            return 0

        target = (1 << k) - 1

        # best[mask][cell] = maximum remaining energy
        best = [[-1] * (m * n) for _ in range(1 << k)]

        sr, sc = start
        start_pos = sr * n + sc

        best[0][start_pos] = energy

        queue = deque()
        queue.append((sr, sc, energy, 0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, remaining, mask, moves = queue.popleft()

            if mask == target:
                return moves

            # Cannot move without energy
            if remaining == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = remaining - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    new_mask |= 1 << litter_id[(nr, nc)]

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                pos = nr * n + nc

                # Only continue if we arrive with MORE energy
                if new_energy > best[new_mask][pos]:
                    best[new_mask][pos] = new_energy
                    queue.append(
                        (nr, nc, new_energy, new_mask, moves + 1)
                    )

        return -1
        