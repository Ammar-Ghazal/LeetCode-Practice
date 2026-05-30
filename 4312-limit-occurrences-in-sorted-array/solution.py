class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        outputArr = []
        countNum = {}

        for n in nums:
            if n in countNum:
                if countNum[n] < k:
                    countNum[n] += 1
                    outputArr.append(n)
            else:
                countNum[n] = 1
                outputArr.append(n)

        return outputArr
