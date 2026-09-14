class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        out = set()
        used = set()

        for i, numi in enumerate(nums):
            if numi in used:
                continue
            
            used.add(numi)
            
            prev = {}

            for j in range(i + 1, len(nums)):
                numj = nums[j]
                numk = -numi - numj

                if numk in prev:
                    out.add(tuple(sorted((numi, numj, numk))))
                
                prev[numj] = j
        
        return [list(triplet) for triplet in out]
