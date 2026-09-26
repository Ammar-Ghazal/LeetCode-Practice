class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flag algorithm
        # Time complexity: O(n)
        # Space complexity: O(1)
        p0 = cur = 0
        p2 = len(nums) - 1

        while cur <= p2:
            if nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
