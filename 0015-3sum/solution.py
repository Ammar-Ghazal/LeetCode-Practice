class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1) -> not counting the allTriplets output
        allTriplets = []
        # sort the nums array so we can plug in 2sum II (version 2) code
        nums.sort()

        # loop for first integer out of the 3 (i, l, r)
        for i in range(len(nums)):
            # check that we aren't at the first index, and if it is a duplicate, skip this itr
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            # initialize the ptr variables for l and r
            l, r = i + 1, len(nums) - 1

            # this here is the code taken from 2sum II (version 2)
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                # if sum is less than 0, update left ptr
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    # sum is equal to 0, add it to the allTriplets list, and update left ptr (doesnt matter which one we update)
                    allTriplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # if the next number is the same, keep updating the left ptr (to avoid duplicates)
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return allTriplets
