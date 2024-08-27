class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r1, r2, r3= 0, 1, 2
        while r1 < (len(nums) - 2):
            if(nums[r1] == nums[r2]):
                if(nums[r2] == nums[r3]):
                    nums.pop(r3)
                else:
                    r1 += 1
                    r2 += 1
                    r3 += 1
            else:
                r1 += 1
                r2 += 1
                r3 += 1


        


        
