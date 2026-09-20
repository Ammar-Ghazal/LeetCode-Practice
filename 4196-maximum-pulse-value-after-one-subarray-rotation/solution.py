class Solution:
    def maxValue(self, nums: List[int]) -> int:
        pulse = nums[0]
        best_gain = 0

        best_even = 2 * nums[0]
        best_odd = 0

        for r in range(1, len(nums)):
            value = nums[r]

            if r % 2 == 0:
                pulse += value
                gain = best_even - 2 * pulse
            else:
                pulse -= value
                gain = best_odd - 2 * pulse

            best_gain = max(best_gain, gain)

            if r%2 == 0:
                best_even = max(best_even, 2* pulse)
                best_odd = max(best_odd, 2* pulse - 2 * value)
            else:
                best_even = max(best_even, 2 * pulse + 2 * value)
                best_odd = max(best_odd, 2 * pulse)


        return pulse + best_gain
