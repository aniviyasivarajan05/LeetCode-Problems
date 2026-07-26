class Solution:
    def computeLPSArray(self, pat):
        n = len(pat)
        lps = [0] * n

        patLen = 0
        i = 1

        while i < n:
            if pat[i] == pat[patLen]:
                patLen += 1
                lps[i] = patLen
                i += 1
            else:
                if patLen != 0:
                    patLen = lps[patLen - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        txt = s + s
        pat = goal

        n = len(txt)
        m = len(pat)

        lps = self.computeLPSArray(pat)

        i = 0
        j = 0

        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1

                if j == m:
                    return True

            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False