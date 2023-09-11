class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        reverse = False
        sList = numRows * [""]
        for i in range(len(s)):
            if i / (numRows - 1) % 2 == 0:
                sList[0] += s[i]
                reverse = False
            elif i / (numRows - 1) % 2 == 1:
                sList[-1] += s[i]
                reverse = True
            else:
                idx = i % (numRows - 1)
                if not reverse:
                    sList[idx] += s[i]
                else:
                    sList[-1-idx] += s[i]

        return "".join(sList)

        