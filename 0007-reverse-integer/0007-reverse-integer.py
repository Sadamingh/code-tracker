class Solution:
    def reverse(self, x: int) -> int:

        neg = False
        if x < 0:
            neg = True
            x *= -1

        x = int(str(x)[::-1])

        if neg:
            x *= -1

        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x