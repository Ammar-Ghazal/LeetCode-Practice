class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(n) or O(s+t), but s==t since we return false otherwise
        # Space Complexity: O(n) or O(s+t)

        if len(s) != len(t): return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        
        return True
