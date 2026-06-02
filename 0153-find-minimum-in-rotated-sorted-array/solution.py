class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time Complexity: O(log(n))
        # Space Complexity: O(1)
        l, r = 0, len(nums) - 1

        # loop terminates when l = m = r, so can return nums[l] or nums[r]
        while l < r:
            m = (l + r) // 2
            # nums[l] <= min <= nums[m]
            if nums[m] < nums[r]:
                r = m
            # nums[m] < min <= nums[r]
            else:
                l = m + 1
        
        return nums[l]
