class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n)
        if len(tokens) == 1: return int(tokens[0])

        # define operations with lambda, and stack to track all solved/pending expressions
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }
        stack = []

        for t in tokens:
            if t in operations:
                r = stack.pop()
                l = stack.pop()
                stack.append(operations[t](l, r))
            else:
                stack.append(int(t))

        return stack[-1]
