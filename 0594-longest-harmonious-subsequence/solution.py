class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        
        longest = 0
        
        for num in nums:
            if (num + 1) in counts:
                longest = max(longest, counts[num] + counts[num + 1])
                
        return longest
