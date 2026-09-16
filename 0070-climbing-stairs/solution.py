class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        # Time complexity: O(n)
        # Spacd complexity: O(n) -> depth of recursion tree can go up to n
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

