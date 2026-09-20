class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()
            
        ans = []
        backtracking([])

        return ans
