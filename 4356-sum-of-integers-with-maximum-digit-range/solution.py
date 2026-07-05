class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxDiff = 0
        output = 0

        def digitRange(n):
            digits = [int(c) for c in str(n)]
            return max(digits) - min(digits)

        # What is current max diff in all digits
        for n in nums:
            maxDiff = max(digitRange(n), maxDiff)

        # Add all numbers with max diff
        for n in nums:
            if digitRange(n) == maxDiff:
                output += n

        return output
            
