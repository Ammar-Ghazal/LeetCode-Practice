class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        laststart, lastend = intervals[0][0], intervals[0][1]
        out = []

        # size = len(intervals)
        # if size == 1 or size == 0: return intervals

        for start, end in intervals:
            if lastend >= start:
                lastend = max(end, lastend)
            else:
                out.append([laststart, lastend])
                laststart = start
                lastend = end
        
        out.append([laststart, lastend])
        
        return out

