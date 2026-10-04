class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(k), k depends on the # of distinct characters in nums

        countNums = Counter(nums)
        maxLen = 0
        for num, count in countNums.items():
            if num + 1 in countNums:
                maxLen = max(maxLen, count + countNums[num + 1])
        
        return maxLen
