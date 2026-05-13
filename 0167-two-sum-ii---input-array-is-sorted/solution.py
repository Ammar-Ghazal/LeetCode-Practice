class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in prevMap:
                return [prevMap[diff]+1, i+1]
            prevMap[numbers[i]] = i


