class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(log(n))
        # Space Complexity: O(1)

        # initialize left, right and middle pointers/indices
        size = len(nums)
        l, r = 0, size - 1

        # if at any point l == r, the binary search has failed to locate target
        while l <= r:
            # update middle every iteration
            m = (l+r)//2

            # update right and left accordingly, and return target if found
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        # failed to locate target
        return -1
