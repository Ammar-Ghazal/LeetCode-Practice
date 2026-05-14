class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        out = [0]*2*len(nums)
        for i in range(len(nums)):
            out[i] = nums[i]

        index = len(nums)
        for j in reversed(range(len(nums))):
            out[index] = nums[j]
            index += 1

        return out
        
