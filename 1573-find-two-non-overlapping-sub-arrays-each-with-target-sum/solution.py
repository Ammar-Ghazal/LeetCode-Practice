class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        answer = float('inf')
        shortest = float('inf')
        curSum = 0
        l = 0

        for r in range(n):
            curSum += arr[r]

            while curSum > target:
                curSum -= arr[l]
                l += 1

            if curSum == target and l <= r:
                currentLength = r - l + 1
                if l > 0:
                    answer = min(answer, currentLength + best[l - 1])
                shortest = min(shortest, currentLength)
            best[r] = shortest

        return -1 if answer == float('inf') else answer
