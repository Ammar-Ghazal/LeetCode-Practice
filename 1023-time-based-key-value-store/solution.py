class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        # Surprise submission failure by lc, must apparently implement binary search :)

        result = ""
        entries = self.timemap[key] # list of tuples
        l, r = 0, len(entries) - 1
        while r >= l:
            m = (l+r)//2
            curval, curtime = entries[m]

            if timestamp == curtime:
                return curval
            elif timestamp > curtime:
                result = curval
                l = m + 1
            else:
                r = m - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
