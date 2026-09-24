class MedianFinder:

    def __init__(self):
        self.small = [] # max heap, min heap using negative vals, has the largest val at the top
        self.large = [] # min heap, has the smallest val at the top

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # send new num to large, and take smallest of large and add to small
            value = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -value)
        else:
            value = -heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return (-self.small[0] + self.large[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
