class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda m: m[1])
        ends = [m[1] for m in meetings]
        pref = []  # pref[k] = max dp over the first k+1 meetings
        ans = float('-inf')
        for s, e, r in meetings:
            w = r - (e - s)
            p = bisect_right(ends, s)  # meetings with end <= s
            best_prev = -s
            if p > 0:
                best_prev = max(best_prev, pref[p - 1])
            cur = w + best_prev
            pref.append(cur if not pref else max(pref[-1], cur))
            ans = max(ans, cur + e)
        return ans
