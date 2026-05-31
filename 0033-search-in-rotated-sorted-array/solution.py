class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            
            # left "sorted" portion of the array
            if nums[l] <= nums[m]: # don't understand why the = is here
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1
            # right sorted portion of the array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

