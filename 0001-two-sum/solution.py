class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) time complexity
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i+1,length):
        #         if i != j:
        #             if nums[i]+nums[j] == target:
        #                 return [i,j]

        # O(n) time complexity
        prevMap = {} # dict that contains all previous numbers that we went over

        for i, n in enumerate (nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i] 
            prevMap[n] = i
        return
            


