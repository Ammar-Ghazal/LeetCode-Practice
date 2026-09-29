class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        maxSize, bestStart = 0, 0
        def expand(l, r):
            nonlocal maxSize, bestStart
            while l >= 0 and r < size and s[l] == s[r]:
                l -= 1
                r += 1
            
            # note that r and l are just outside the palindrome
            if r - l - 1 > maxSize:
                maxSize = r - l - 1
                bestStart = l + 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[bestStart:bestStart+maxSize]
