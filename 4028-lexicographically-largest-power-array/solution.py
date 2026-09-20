class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        groups = [nums]
        power = []

        for bit in range(14, -1, -1):
            count = 0

            for i in range(len(groups)):
                ones = []
                zeros = []

                for num in groups[i]:
                    if num & (1<<bit):
                        ones.append(num)
                    else:
                        zeros.append(num)

                count += len(ones)

                if zeros:
                    if ones:
                        groups[i:i+1] = [ones, zeros]
                    break

            power.append(count)

        return power
