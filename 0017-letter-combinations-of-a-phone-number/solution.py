class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Time complexity: O(n * 4^n), n is length of digits, 4 is max # of letters in numToLetters (7 & 9)
        # Space complexity: O(n), only n function calls can be in the stack at once, although 4^n run in total
        numToLetters = {"2":"abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        letterCombinations = []

        if not digits: return []

        def combinator(remainingDig, curComb):
            if remainingDig == "":
                letterCombinations.append(curComb)
                return
            leftDigit = remainingDig[0]
            for letter in numToLetters[leftDigit]: # this here adds 4^n time & n space complexity (call stacks), worst case is digits is only 7s & 9s
                combinator(remainingDig[1:], curComb + letter)
            
        combinator(digits, "")

        return letterCombinations


