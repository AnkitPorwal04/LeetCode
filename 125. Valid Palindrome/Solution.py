class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                a += i
        if a == a[::-1]:
            return True
        else:
            return False
