class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        curlist = self.map[key]
        l, r = 0, len(curlist) - 1
        lastval = ""
        
        while l <= r:
            m = (l + r) // 2
            curval, curtime = curlist[m]
            if curtime == timestamp:
                return curval
            elif curtime < timestamp:
                l = m + 1
                lastval = curval
            else:
                r = m - 1
        
        return lastval

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
