class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        size = len(nums)
        out = [0]*size*2

        for i in range(size*2):
            out[i] = nums[i%size]

        return out
