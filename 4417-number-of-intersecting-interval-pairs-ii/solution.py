class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intersects = 0
        ended = 0

        starts = sorted(start for start, end in intervals)
        ends = sorted(end for start, end in intervals)

        for i in range(len(starts)):
            while ends[ended] < starts[i]:
                ended += 1
            intersects += i - ended

        return intersects
