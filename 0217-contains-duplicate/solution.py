class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)
        visited = set()
        for num in nums:
            if num in visited: return True
            visited.add(num)
        return False
