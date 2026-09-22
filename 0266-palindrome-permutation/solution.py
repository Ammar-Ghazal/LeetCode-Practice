class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
#         only one char can have an odd number of occurunces, the rest must be even, or all are even
        counts = Counter(s)
        oddExists = False
        
        for char in counts:
            if counts[char] % 2 != 0:
                if oddExists:
                    return False
                oddExists = True
        
        return True
