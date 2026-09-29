class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Time complexity: O(N*2^N)
            # we need to create 2^N subsets, and the .copy takes N time depending on the length of nums
        # Space complexity: O(N*2^N)
            # we store 2^N subsets, for a total of N*2^(N-1) elements, big O notation ignores constant factors, so its O(N*2^N)
        out = [[]]

        for num in nums:
            newSubsets = []
            for cur in out:
                temp = cur.copy()
                temp.append(num)
                newSubsets.append(temp)
            for cur in newSubsets:
                out.append(cur)
        return out
