class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            word = set()
            for j in range(i,len(s)):
                if s[j] in word:
                    break
                word.add(s[j])
            res = max(res,len(word))
        return res
