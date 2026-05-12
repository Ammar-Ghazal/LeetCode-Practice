class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(s+t)
        # Space Complexity: O(n), up to n unique characters depending on s and t

        # pythonic solution:
        return Counter(s) == Counter(t)

        # pythonic solution with O(1) space complexity (assuming sorting algorithm doesnt take space in memory), note that sorting algorithm method worsens time complexity to O(n^2)/O(nlog(n)), depending on which one is used
        # return sorted(s) == sorted(t)

        # check that they are the same length:
        if len(s) != len(t):
            return False

        # create hashmaps to store all characters and their counts
        countS, countT = {}, {}

        # populate the hashmaps with the characters and counts
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        
        # check if the character hashmaps are equal, if they are not, return false
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
