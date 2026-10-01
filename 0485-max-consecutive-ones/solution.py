class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max1 = 0
        cur1 = 0

        for num in nums:
            if num == 1:
                cur1 += 1
            else:
                max1 = max(max1, cur1)
                cur1 = 0

        return max(max1, cur1)
