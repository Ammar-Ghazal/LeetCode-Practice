class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time complexity: O(n) n is the length of the string inputted
        # Space complexity: O(m) m is the length of the alphabet used
        maxChar, l = 0, 0
        visited = set()
        size = len(s)

        for cur in s:
            while cur in visited:
                visited.remove(s[l])
                l += 1
            visited.add(cur)
            maxChar = max(maxChar, len(visited))
        
        return maxChar

