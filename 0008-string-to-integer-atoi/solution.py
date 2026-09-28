class Solution:
    def myAtoi(self, s: str) -> int:
        i, outNum, sign, size = 0, 0, 1, len(s)
        limit = 0

        # skip leading whitespaces
        while i < size and s[i] == " ":
            i += 1
        
        # determine sign
        if i < size and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # set the limit, depending on the sign
        if sign == -1:
            limit = 2**31
        else:
            limit = 2**31 - 1
        
        while i < size and "0" <= s[i] <= "9":
            outNum = outNum * 10 + int(s[i])
            if outNum > limit:
                return sign*limit
            i += 1
        
        return sign * outNum
        
