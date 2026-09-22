class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        
        
        for i in range(size//2):
            temp = s[i]
            s[i] = s[size - 1 - i]
            s[size - 1 -i] = temp
