from bisect import bisect_left


class Solution:
    def validSequence(self, word1: str, word2: str):
        n, m = len(word1), len(word2)

        # Store positions of every character in word1
        positions = {}
        for i, ch in enumerate(word1):
            positions.setdefault(ch, []).append(i)

        # ---------------------------------------------------------
        # run_start[i] = first index of the consecutive block
        # containing i
        #
        # Example: word1 = "aaabbc"
        # run_start = [0,0,0,3,4,5]
        # ---------------------------------------------------------
        run_start = [0] * n

        for i in range(n):
            if i == 0 or word1[i] != word1[i - 1]:
                run_start[i] = i
            else:
                run_start[i] = run_start[i - 1]

        # ---------------------------------------------------------
        # exact[j] = rightmost possible position of word2[j]
        # such that word2[j:] can be matched EXACTLY.
        #
        # -1 means impossible.
        # exact[m] = n means empty suffix is always possible.
        # ---------------------------------------------------------
        exact = [-1] * (m + 1)
        exact[m] = n

        for j in range(m - 1, -1, -1):
            bound = exact[j + 1]

            if bound < 0:
                continue

            arr = positions.get(word2[j], [])

            # Find rightmost occurrence < bound
            k = bisect_left(arr, bound)

            if k > 0:
                exact[j] = arr[k - 1]

        # ---------------------------------------------------------
        # one[j] = rightmost possible position of word2[j]
        # such that word2[j:] can be matched with AT MOST
        # one mismatch.
        #
        # one[m] = n because empty suffix needs no characters.
        # ---------------------------------------------------------
        one = [-1] * (m + 1)
        one[m] = n

        for j in range(m - 1, -1, -1):
            target = word2[j]

            # Case 1:
            # Current character matches.
            # Remaining suffix may use the one allowed mismatch.
            bound = one[j + 1]

            if bound >= 0:
                arr = positions.get(target, [])
                k = bisect_left(arr, bound)

                if k > 0:
                    one[j] = max(one[j], arr[k - 1])

            # Case 2:
            # Use the one mismatch at the current character.
            # Therefore the remaining suffix must match exactly.
            bound = exact[j + 1]

            if bound > 0:
                p = bound - 1

                # We need word1[p] != target.
                # If it equals target, move to the beginning
                # of that consecutive run.
                if word1[p] == target:
                    p = run_start[p] - 1

                if p >= 0:
                    one[j] = max(one[j], p)

        # ---------------------------------------------------------
        # Construct lexicographically smallest answer.
        #
        # We scan word1 from left to right.
        # The first valid index we can take is always optimal.
        # ---------------------------------------------------------
        ans = []
        i = 0
        mismatch_used = 0

        for j in range(m):
            target = word2[j]
            found = False

            while i < n:

                # Case 1: Current character matches
                if word1[i] == target:

                    # Remaining part can be completed with
                    # at most one mismatch.
                    if one[j + 1] > i:
                        ans.append(i)
                        i += 1
                        found = True
                        break

                # Case 2: Current character does not match
                else:
                    # We can use our single mismatch here.
                    if mismatch_used == 0 and exact[j + 1] > i:
                        ans.append(i)
                        i += 1
                        mismatch_used = 1
                        found = True
                        break

                i += 1

            if not found:
                return []

        return ans