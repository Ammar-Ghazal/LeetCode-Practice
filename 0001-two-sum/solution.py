class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        prevMap = {} # numbers must be set as keys to perform if check in O(1) time
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[nums[i]] = i

        # O(n2) implementation:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
