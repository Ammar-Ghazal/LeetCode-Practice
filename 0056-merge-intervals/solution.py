class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(nlog(n)) -> due to sorting used
        # Space Complexity: O(1) -> if we exclude the output of merge

        # sort the intervals by their starting value, it will be easier to work with
        intervals.sort(key=lambda x: x[0])
        # initialize variables, stream is to indicate if the current interval connects to the next interval
        merged = []
        stream = False
        start = end = 0
        
        # loop through all the intervals
        for i in range(len(intervals) - 1):
            # curr and next store current interval values
            curr = intervals[i]
            nxt = intervals[i + 1]
            
            # if the intervals are not connected, set start and end values
            if not stream:
                start, end = curr[0], curr[1]
            
            # if the interval is connected, set stream to true and update end value
            if end >= nxt[0]:                # next overlaps with our window
                stream = True
                end = max(end, nxt[1])       # extend the window
            # otherwise, add the start and end to the list and set stream to false
            else:
                merged.append([start, end])  # commit the window
                stream = False
        
        # commit whatever's still open at the end
        merged.append([start, end] if stream else intervals[-1])
        
        return merged
