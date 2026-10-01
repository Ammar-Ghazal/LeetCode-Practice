class Solution:
    def calculate(self, s: str) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        cur = 0
        total = 0
        sign = 1 # 1 is positive, -1 is negative

        for char in s:
            if char.isdigit():
                cur = (cur)*10 + int(char)
            elif char == "+":
                total += sign * cur
                sign = 1
                cur = 0 # must be reset for any time char isnt a number
            elif char == "-":
                total += sign * cur
                sign = -1
                cur = 0
            elif char == "(":
                stack.append(total)
                stack.append(sign)
                sign = 1
                total = 0
            elif char == ")":
                total += sign * cur
                total *= stack.pop() # this is the last sign, +1 by default
                total += stack.pop()
                cur = 0
                # sign = 1 # this is apparently redundant since cur is now 0
                # sign will reset anyways in the next +/-, if not, the cur is 0 so += sign * cur does nothing
            
        return total + sign * cur            
