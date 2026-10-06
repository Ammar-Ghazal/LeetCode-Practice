class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time complexity: O(n^2)
        # Space complexity: O(1), since we only store bestStart and maxLen, not a whole substring
        maxLen, bestStart = 0, 0
        size = len(s)

        def looper(i, j):
            nonlocal maxLen, bestStart
            while i >= 0 and j < size and s[i] == s[j]:
                # print(f"(i, j): ({i}, {j})")
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    bestStart = i
                i -= 1
                j += 1

        for i in range(size):
            looper(i, i)
            looper(i, i + 1)

        return s[bestStart : bestStart + maxLen ]
