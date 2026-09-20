class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intersects = 0
        length = len(intervals)
        for i in range(length):
            for j in range(i + 1, length):
                if intervals[i][1] >= intervals [j][0] and intervals[i][0] <= intervals[j][1]:
                    intersects += 1

        return intersects
