class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums[:]:
            if (val == num):
                nums.remove(num)

        
