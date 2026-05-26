class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ------------- Implementation #1 -------------
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i+1,length):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # ---------------------------------------------

        # ------------- Implementation #2 -------------
        # Time complexity: O(n)
        # Space complexity: O(n)
        prevSum = {} # to save old numbers

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevSum:
                return [prevSum[diff], i]
            prevSum[nums[i]] = i
        # ---------------------------------------------
