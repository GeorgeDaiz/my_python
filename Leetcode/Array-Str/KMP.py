class Solution:
    def build_nxt(self, p):  # abaabcac
        i = 0
        j = -1
        nxt = [-1] * len(p)

        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                if i < len(p) and p[i] != p[j]:
                    nxt[i] = j
                else:
                    nxt[i] = nxt[j]
            else:
                j = nxt[j]
        return nxt

    def kmp(self, s, p):
        i = 0
        j = 0
        nxt = self.build_nxt(p)
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]

        if j == len(s):
            return i - j
        else:
            return -1
