class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        # extract the start and end values, and sort them separately
        starts = sorted(start for start, end in intervals)
        ends = sorted(end for start, end in intervals)

        out, ended = 0, 0

        for i, start in enumerate(starts):
            while ends[ended] < start:
                ended += 1
            # for each interval, i intervals have started
            # subtract from those the intervals that have already ended,
            # and you have the total intersecting intervals for the current interval
            out += i - ended

        return out
