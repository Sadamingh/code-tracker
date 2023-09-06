class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        maxLen = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    maxLen = len(s[i:j+1]) if len(s[i:j+1]) > maxLen else maxLen
                else:
                    break
        
        return maxLen