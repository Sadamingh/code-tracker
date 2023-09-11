class Solution:

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        p = ""

        for i in range(len(s)):
            p1 = self.expSearch(i, i)
            p2 = self.expSearch(i, i+1)

            if  len(p1) > len(p):
                p = p1
            if  len(p2) > len(p):
                p = p2

        return p

    def expSearch(self, left, right):
        result = ""
        while left >= 0 and right < len(self.s):
            if self.s[left] == self.s[right]:
                result = self.s[left:right+1]
                left -= 1
                right += 1
            else:
                break
        return result
