class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char.lower() for char in s if char.isalnum())
        res = text[::-1]

        if text==res:
            return True
        else:
            return False