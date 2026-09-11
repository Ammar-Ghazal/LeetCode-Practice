class Solution:
    # def alphaNum(self, c: str) -> bool:
    #     return (
    #         'A' <= c <= 'Z' or
    #         'a' <= c <= 'z' or
    #         '0' <= c <= '9'
    #     )

    def isPalindrome(self, s: str) -> bool:
        # l, r = 0, len(s) - 1

        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l, r = l + 1, r - 1
        
        # return True

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        clean = "".join(filter(str.isalnum, s)).lower()
        return clean == clean[::-1]
