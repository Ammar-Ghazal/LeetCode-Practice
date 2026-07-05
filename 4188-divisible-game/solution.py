
class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        l, r = 0, 0
        MOD = 10**9 + 7
        maxScoreDiff, bestK = None, None
        kVals = {2}

        # get k vals
        for n in nums:
            d = 2
            while d**2 <= n:
                if n % d == 0:
                    kVals.add(d)
                    kVals.add(n // d)
                d += 1
            if n > 1:
                kVals.add(n)

        # calculate max score and decide on k val
        for k in sorted(kVals):
            l, r = 0, 0
            scoreDiff = 0

            for r in range(len(nums)):
                scoreDiff += nums[r] if nums[r] % k == 0 else -nums[r]
                if maxScoreDiff is None or scoreDiff > maxScoreDiff:
                    maxScoreDiff = scoreDiff
                    bestK = k
                if scoreDiff < 0:
                    l = r + 1
                    scoreDiff = 0

        return (maxScoreDiff * bestK) % MOD
