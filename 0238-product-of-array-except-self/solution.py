class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time complexity: O(n), n -> len(nums)
        # Space complexity: O(1), unless you count output then its O(n)
        size = len(nums)
        output = [0]*size

        rightSweep = 1
        for i in range(size):
            output[i] = rightSweep
            rightSweep *= nums[i]
        
        leftSweep = 1
        for i in range(size-1, -1, -1):
            output[i] *= leftSweep
            leftSweep *= nums[i]
        
        return output
