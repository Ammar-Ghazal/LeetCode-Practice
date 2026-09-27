class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        keys = sorted(cnt)
        ans = []

        for i in range(max(cnt.values())):
            for k in keys:
                if cnt[k] > i:
                    ans.append(k)

        return ans
