class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        out = []
        i = 0
        size = len(intervals)
        
        # first, keep going through the intervals, until we reach the point where we want to enter newInterval
        while i < size and newInterval[0] > intervals[i][1]:
            out.append(intervals[i])
            i += 1
        
        # now add the current interval, and keep extending the added interval until it covers the last overlapped interval
        start = newInterval[0]
        end = newInterval[1]

        while i < size and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        # now make the addition of the newInterval, with modified end value to contain overlapped intervals
        out.append([start, end])

        # add the rest of the intervals
        while i < size:
            out.append(intervals[i])
            i += 1
        
        return out
