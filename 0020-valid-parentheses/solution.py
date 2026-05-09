class Solution:
    def isValid(self, s: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Use stack to keep track of ordering of opening braces
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s:
            # If character is closing brace
            if c in closeToOpen:
                # if it is a closing brace and the stack is empty it isnt valid
                if not stack:
                    return False
                # if last opening brace matches current closing brace, remove opening brace
                elif stack[-1] == closeToOpen[c]:
                    stack.pop()
                # if the braces doesnt match, it isnt valid
                else:
                    return False
            # if it is an opening brace, add it to the stack
            else:
                stack.append(c)
               
        # if the stack is empty, return true, otherwise return false
        return not stack
