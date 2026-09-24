class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Time complexity: O(n log n) worst case
        # Space complexity: O(n)
        # by definition, since number of instances is > n/2
        # the majority element will always be in the middle
        mid = int(len(nums)/2)
        return sorted(nums)[mid]
