class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        M = 500
        cnt = [0] * (M + 1)

        def conflicts(v: int) -> bool:
            # v as the sum: a + b = v
            for a in range(1, v // 2 + 1):
                b = v - a
                if a == b:
                    if cnt[a] >= 2:
                        return True
                elif cnt[a] and cnt[b]:
                    return True
            # v as an addend: v + w = u
            for w in range(1, M - v + 1):
                if cnt[w] and cnt[v + w]:
                    return True
            return False

        best = l = 0
        for r, v in enumerate(nums):
            while conflicts(v):
                cnt[nums[l]] -= 1
                l += 1
            cnt[v] += 1
            best = max(best, r - l + 1)
        return best
