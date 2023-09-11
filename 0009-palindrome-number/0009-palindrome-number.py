class Solution:
    def isPalindrome(self, x: int) -> bool:

        digiList = []

        if x < 0:
            return False
        
        while x > 0:
            digiList.append(x % 10)
            x = x // 10
        
        if digiList == digiList[::-1]:
            return True
        
        return False


            