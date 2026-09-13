# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, out = 1, n, n

        while r >= l:
            m = (l+r)//2
            if isBadVersion(m):
                out = m
                r = m - 1
            else:
                l = m + 1

        return out
