class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        maxProd, forProd, backProd = nums[0], 1, 1
        length = len(nums)

        for i in range(length):
            forProd *= nums[i]
            backProd *= nums[length - i - 1]
            maxProd = max(maxProd, max(forProd, backProd))

            if forProd == 0: forProd = 1
            if backProd == 0: backProd = 1

        return maxProd
