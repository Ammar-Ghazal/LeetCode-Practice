class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = 0
        pairs = Counter()
        for a, b in zip(nums, nums[1:]):
            if a == b:
                base += 1
            else:
                pairs[(min(a, b), max(a, b))] += 1
        return base + max(pairs.values(), default=0)
