class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_val = max(nums)
        present = set(nums)
        smallest_divisor = [0] * (max_val + 1)
        
        # For each value v in nums (ascending), mark v as the smallest
        # divisor for every unmarked multiple of v up to max_val.
        for v in sorted(present):
            for multiple in range(v, max_val + 1, v):
                if smallest_divisor[multiple] == 0:
                    smallest_divisor[multiple] = v
        
        return sum(smallest_divisor[num] for num in nums)
