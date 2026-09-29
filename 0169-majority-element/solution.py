class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # boyer moore algo for the below complexities, only works if majority element has more than n/2 occurences
        # Time complexity: O(n)
        # Space complexity: O(1)

        candidate, count = None, 0

        for n in nums:
            if count == 0:
                candidate = n

            if candidate == n:
                count += 1
            else:
                count -= 1

        return candidate
