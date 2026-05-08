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
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            # we are mapping the values as the key to perform this check in O(1) time
            if diff in prevMap:
                return[prevMap[diff], i]
            else:
                prevMap[n] = i
        return
        # ---------------------------------------------
