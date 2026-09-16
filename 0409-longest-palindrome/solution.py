class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        counter = defaultdict(int)
        gotodd = False

        for c in s:
            counter[c] += 1

        counter = dict(sorted(counter.items(), key=lambda item: item[1]))

        for char, occ in counter.items():
            if occ%2 == 0:
                count += occ
                # print("we got even number, count: " + str(count) + " char: " + char)
            else:
                count += occ - 1
                # print("we got odd number, count: " + str(count) + " char: " + char)
                gotodd = True

        if gotodd:
            count += 1
        
        # print(counter)
        return count
