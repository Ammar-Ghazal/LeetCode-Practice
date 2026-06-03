import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        count = {}
        l, maxRep = 0, 1

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maxRep = max(r - l + 1, maxRep)
            
        return maxRep
