class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        visited = set()
        l, maxSub = 0, 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            maxSub = max(r - l + 1, maxSub)
            visited.add(s[r])
        
        return maxSub


        # # Second Implementation
        # # Time Complexity: O(n)
        # # Space Complexity: O(1)
        # count = {}
        # l, maxSub = 0, 0

        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     while count[s[r]] > 1:
        #         count[s[l]] -= 1
        #         l += 1
        #     maxSub = max(r-l+1, maxSub)
    
        # return maxSub
