class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listsize = len(nums)
        for i in range(listsize):
            for j in range(listsize):
                if(i != j):
                    if(nums[i] + nums[j] == target):
                        return [i,j]
