class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        # Each node stores: (max_len, pref_len, suff_len, pref_char, suff_char, seg_len)
        self.tree = [None] * (4 * self.n)
        self._build(s, 1, 0, self.n - 1)

    def _merge(self, left, right):
        l_max, l_pref, l_suff, l_pchar, l_schar, l_len = left
        r_max, r_pref, r_suff, r_pchar, r_schar, r_len = right

        seg_len = l_len + r_len
        
        # Calculate prefix length
        pref_char = l_pchar
        pref_len = l_pref + (r_pref if l_pref == l_len and l_pchar == r_pchar else 0)

        # Calculate suffix length
        suff_char = r_schar
        suff_len = r_suff + (l_suff if r_suff == r_len and r_schar == l_schar else 0)

        # Calculate maximum contiguous block length
        max_len = max(l_max, r_max)
        if l_schar == r_pchar:
            max_len = max(max_len, l_suff + r_pref)

        return (max_len, pref_len, suff_len, pref_char, suff_char, seg_len)

    def _build(self, s: str, node: int, start: int, end: int):
        if start == end:
            ch = s[start]
            self.tree[node] = (1, 1, 1, ch, ch, 1)
            return
        
        mid = (start + end) // 2
        self._build(s, 2 * node, start, mid)
        self._build(s, 2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, idx: int, ch: str):
        self._update(1, 0, self.n - 1, idx, ch)

    def _update(self, node: int, start: int, end: int, idx: int, ch: str):
        if start == end:
            self.tree[node] = (1, 1, 1, ch, ch, 1)
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, ch)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, ch)
            
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def get_max_len(self) -> int:
        return self.tree[1][0]


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(idx, ch)
            ans.append(st.get_max_len())
            
        return ans