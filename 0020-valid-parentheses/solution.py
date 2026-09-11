class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = False
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for b in s:
            if b in closeToOpen: # this is a closing brace
                if stack and closeToOpen[b] == stack[-1]: # current brace matches last opening brace
                    stack.pop() # remove the matching closing brace
                else:
                    return False
            else: # must be an opening brace
                stack.append(b)
        
        # returns true if the stack is empty, and false otherwise
        return not stack
