class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        sCount, tCount = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        # print(sCount, tCount)
        return sCount == tCount  
