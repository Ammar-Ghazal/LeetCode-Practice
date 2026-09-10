class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in prev:
                return [prev[n], i]
            prev[nums[i]] = i
            # prev[n] - i

