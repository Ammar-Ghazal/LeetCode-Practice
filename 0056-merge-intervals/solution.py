class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(nlog(n)) -> from sorting
        # Space Complexity: O(n)
        intervals.sort()
        output = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)-1):
            if end < intervals[i+1][0]:
                output.append([start, end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]
            else:
                if end < intervals[i+1][1]:
                    end = intervals[i+1][1]

        output.append([start, end])
        
        return output
