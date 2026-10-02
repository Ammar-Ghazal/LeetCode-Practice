class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [start for start, end, gain in jobs]
        n = len(jobs)

        dp = [0] * (n + 1)
        # note: the n + 1 index simply acts as a placeholder index for holding 0 for when there is not alternate interval, if bisect_left finds no suitable index, it returns n + 1 by default

        for i in range(n - 1, -1, -1):
            start, end, gain = jobs[i]

            # next job that starts at or after the current job ends
            nextJob = bisect_left(starts, end)
            
            # make either decision to take it or leave it
            take = gain + dp[nextJob]
            skip = dp[i + 1]

            dp[i] = max(take, skip)

        return dp[0]

