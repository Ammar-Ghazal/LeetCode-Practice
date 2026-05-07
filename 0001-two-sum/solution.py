class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) time complexity, O(1) space complexity
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i+1, length):
        #         if i != j:
        #             if nums[i]+nums[j] == target:
        #                 return [i,j]
        
        # O(n) time complexity, O(n) space complexity (in the worst case that every value need be stored in the hashmap)
        # contains all previous numbers that we went over
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            #we put the numbers in the keys so we can perform this check in O(1) time
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return




