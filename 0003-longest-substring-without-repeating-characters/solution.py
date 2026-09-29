class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest, l = 0, 0

        for cur in s:
            while cur in visited:
                visited.remove(s[l])
                l += 1

            visited.add(cur)
            longest = max(longest, len(visited))

        return longest
