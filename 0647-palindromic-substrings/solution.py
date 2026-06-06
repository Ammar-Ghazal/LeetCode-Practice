class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time Complexity: O(n^3), because the reversing of the string takes O(n) time
        # Space Complexity: O(n), for storing each of the substrings s[i:j] and their reverses s[i:j][::-1]
        output = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # unique substrings are s[i:j]
                if s[i:j] == s[i:j][::-1]:
                    output += 1
        
        return output
