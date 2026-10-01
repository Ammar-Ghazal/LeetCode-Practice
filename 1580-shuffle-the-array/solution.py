class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half1 = nums[:n]
        half2 = nums[n:]

        i1 = 0
        i2 = 1

        for j in range(n):
            nums[i1] = half1[j]
            nums[i2] = half2[j]
            i1 += 2
            i2 += 2

        return nums
