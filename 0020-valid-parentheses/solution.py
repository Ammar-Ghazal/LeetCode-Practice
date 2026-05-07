class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        for char in s:
            # check if it is a closing brace
            if char in closeToOpen: 
                if not stack: # if closing brace and stack is empty, return False
                    return False 
                # if current closing brace matches last opening brace, remove it from the stack
                elif closeToOpen[char] == stack[-1]:
                    stack.pop()
                else: # if it doesn't match, return false
                    return False
            # if not closing brace, must be an opening brace, add to stack
            else:
                stack.append(char)

        # if the stack is still empty, return true, otherwise return false
        return not stack
