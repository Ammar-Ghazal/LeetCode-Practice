class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time complexity: O(2^(t/m)), t -> target, m -> minimum value in nums
        # Space complexity: O(t/m)
        out = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                out.append(cur.copy()) 
                return
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)

        return out

        
# New code:
# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         # Time complexity: O(2^(t/m)), t -> target, m -> minimum value in nums
#         # Space complexity: O(t/m)
#         out = []

#         def dfs(i, cur, total):
#             if total == target:
#                 out.append(cur.copy())
#                 return
#             if i >= len(candidates) or total > target:
#                 return

#             cur.append(candidates[i])
#             dfs(i, cur, total + candidates[i])
#             cur.pop()
#             dfs(i + 1, cur, total)

#         dfs(0, [], 0)

#         return out
