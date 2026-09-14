class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time complexity: O(n) n is the length of the string inputted
        # Space complexity: O(m) m is the length of the alphabet used
        maxSub, l = 0, 0
        strLen = len(s)
        visited = set()
        
        for char in s:
            while char in visited:
                visited.remove(s[l])
                l += 1
            visited.add(char)
            maxSub = max(maxSub, len(visited))
        return maxSub
