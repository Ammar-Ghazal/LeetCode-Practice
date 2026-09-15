class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        size = len(s)
        palindromes = []
        # find all palindromes of at least size k
        for i in range(size):
            for j in range(i + k, min(i + k + 2, size + 1)):
                if self.isPalindrome(s[i:j]):
                    palindromes.append((i,j))
        
        # remove touching palindromes
        # first sort by ending position, to maximize space for other palindromes
        palindromes.sort(key=lambda p: p[1])
        count = 0
        previousEnd = 0

        for start, end in palindromes:
            # = is allowed here since s[1:3] and s[3:5] touch but dont share a character
            if start >= previousEnd:
                count += 1
                previousEnd = end

        return count
        
    def isPalindrome(self, s: str):
        return s == s[::-1]
