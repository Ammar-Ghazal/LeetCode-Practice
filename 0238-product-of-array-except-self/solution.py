class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1) -> excluding the output array needed for the problem

        # Initialize output array, prefix & postfix values
        output = [1]*len(nums)
        prefix, postfix = 1, 1
        # prefix = product of all elements before index i (computed left-to-right)
        # postfix = product of all elements after index i (computed right-to-left)

        for i in range(len(nums)):
            output[i] = prefix # small optimization here, replacing '*= prefix' with '= prefix'
            prefix *= nums[i]

        for j in reversed(range(len(nums))):
            output[j] *= postfix
            postfix *= nums[j]

        return output

