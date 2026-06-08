class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        def paliCounter(s: str, l: int, r: int ) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += paliCounter(s, i, i)
            count += paliCounter(s, i, i + 1)
        
        return count
