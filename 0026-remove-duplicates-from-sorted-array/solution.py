class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r1, r2, = 0, 1

        while r1 < (len(nums) - 1):
            if(nums[r1] == nums[r2]):
                nums.pop(r2)
            else:
                r1 += 1
                r2 += 1


        
