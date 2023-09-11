class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0

        sign = None

        if s[0] == '+' or s[0] == '-':
            sign = s[0]
            s = s[1:]
        
        sDigi = ""
        for i in s:
            if ord(i) >= 48 and ord(i) <= 57:
                sDigi += i
            else:
                break

        if sDigi != '':
            d = int(sDigi)
        else:
            d = 0


        if sign == "-":
            d *= -1

        if d < -2**31:
            return -2**31
        if d > 2**31 - 1:
            return 2**31 - 1
        
        return d