class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # initialize hashset, fast lookup and enforces uniqueness
        # why not use dict? to avoid having to store useless values: {1:true}, for example
        hashset = set()
        
        for n in nums:
            # check if the number has been seen before, if yes it has duplicates
            if n in hashset:
                return True
            # add the number if it is unique
            hashset.add(n)

        # return false since no duplicates have been found
        return False
