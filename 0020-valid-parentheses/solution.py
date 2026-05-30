class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for b in s:
            if b in closeToOpen:
                if stack and closeToOpen[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return not stack

        
