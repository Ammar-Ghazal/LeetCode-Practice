class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        maxProd = nums[0]
        curProd = 1

        # no idea how this works or what I did, i just drooled on my keyboard and it passed
        # goodluck to future me who has to write the comments

        for i in range(len(nums)):
            if curProd == 0:
                curProd = 1
            curProd *= nums[i]
            maxProd = max(curProd, maxProd)
        
        curProd = 1
        for j in reversed(range(len(nums))):
            if curProd == 0:
                curProd = 1
            curProd *= nums[j]
            maxProd = max(curProd, maxProd)

        return maxProd
