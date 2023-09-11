class Solution:
    def isPalindrome(self, x: int) -> bool:

        digiList = []

        if x < 0:
            return False
        
        while x > 0:
            digiList.append(x % 10)
            x = x // 10
        
        return digiList == digiList[::-1]
