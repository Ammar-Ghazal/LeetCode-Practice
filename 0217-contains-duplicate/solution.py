class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        pastNums = set()
        for n in nums:
            if n in pastNums:
                return True
            pastNums.add(n)
        return False

