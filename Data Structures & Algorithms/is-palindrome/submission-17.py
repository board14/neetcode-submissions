class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr=""
        for i in range(len(s)):
            if s[i].isalnum():
                nstr+=s[i].lower()
        return nstr==nstr[::-1]
        