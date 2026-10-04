class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space compelxity: O(1) -> O(k), k is the number of letters being used, limited by alphabet size since k is finite, its O(1)
        if len(s) != len(t): return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for ch, count in countS.items():
            if countT.get(ch, 0) != count: return False
        
        return True
