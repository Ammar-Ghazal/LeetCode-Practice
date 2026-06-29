from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):              # early exit, skips all work for impossible cases
            return ""
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        res, resLen = (-1, -1), float("inf")   # store indices, not the substring
        l = 0
        for r, c in enumerate(s):        # for-loop + enumerate, no manual r bookkeeping
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:          # inner while shrinks fully before expanding again
                if (r - l + 1) < resLen:
                    res = (l, r)
                    resLen = r - l + 1
                lc = s[l]
                window[lc] -= 1
                if lc in countT and window[lc] < countT[lc]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
