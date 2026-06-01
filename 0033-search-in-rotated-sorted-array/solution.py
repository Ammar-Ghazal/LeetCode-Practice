class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # check if right portion of nums is sorted:
            if nums[l] <= nums[m]:
                # check if target is within sorted portion:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if left portion is unsorted, then right portion must be sorted:
            else:
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1
