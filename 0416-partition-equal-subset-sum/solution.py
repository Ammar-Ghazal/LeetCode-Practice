class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # Time complexity: O(n*t), n = len(nums), t = target
        # Space complexity: O(n*t)
        totalSum = 0
        for num in nums:
            totalSum += num
        if totalSum % 2 != 0: return False
        target = totalSum / 2
        
        @cache
        def dp(total, index):
            if total == target: return True
            elif index == len(nums) or total > target: return False

            return (dp(total + nums[index], index + 1)
                or dp(total, index + 1))
        
        return dp(0, 0)
