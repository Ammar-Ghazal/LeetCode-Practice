class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time complexity: O(m*n) n is length of ransomNote and m is the length of magazine
        # Space complexity: O(m) we need to create magazine, size m
        for c in ransomNote:
            if c not in magazine: return False
            magazine = magazine.replace(c, "", 1)
        return True
