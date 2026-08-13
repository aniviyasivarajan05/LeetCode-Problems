class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        # (left_char, right_char, prefix, suffix, best, length)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, pre1, suf1, best1, len1 = a
            lc2, rc2, pre2, suf2, best2, len2 = b

            # Prefix
            pre = pre1
            if pre1 == len1 and lc1 == lc2:
                pre = len1 + pre2

            # Suffix
            suf = suf2
            if suf2 == len2 and rc1 == rc2:
                suf = suf1 + len2

            # Best answer
            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

            return (lc1, rc2, pre, suf, best, len1 + len2)

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, c):
            if l == r:
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, c)
            else:
                update(node * 2 + 1, mid + 1, r, idx, c)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, c)
            ans.append(tree[1][4])

        return ans