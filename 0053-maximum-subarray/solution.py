class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # initialize one variable to track current sum, and another for overall highest sum
        curNum = 0
        maxNum = nums[0]

        # for all numbers, check if they improve the curent sum, if not, reset curNum and keep looking
        for n in nums:
            # if curNum is ever negative, set it back to 0 and keep looking for highest sum
            if curNum < 0:
                curNum = 0
            # add current num to latest summation series
            curNum += n
            # if current summation is highest, save it
            maxNum = max(curNum, maxNum)

        # return highest summation
        return maxNum
