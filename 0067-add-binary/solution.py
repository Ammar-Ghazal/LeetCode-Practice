class Solution:
    def addBinary(self, a: str, b: str) -> str:
        numa, numb = 0, 0

        for digit in a:
            numa = numa * 2 + int(digit)
        for digit in b:
            numb = numb * 2 + int(digit)

        outnum = numa + numb

        result = ""
        while outnum > 0:
            outnum, remainder = divmod(outnum, 2)
            result = str(remainder) + result
        
        if result == "": return "0"
        return result
