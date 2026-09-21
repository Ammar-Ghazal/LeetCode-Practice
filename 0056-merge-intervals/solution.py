class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        out = []
        intervals.sort(key = lambda x: x[0])

        for start, end in intervals:
            if not out or start > out[-1][1]:
                out.append([start, end])
            else:
                out[-1][1] = max(out[-1][1], end)
        
        return out
