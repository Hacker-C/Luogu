class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def f(x):
            if '0'<=x<='9' or 'a'<=x<='z' or 'A'<=x<='Z':
                return x
        s = list(filter(f, s))
        if list(reversed(s))==s:
            return True
        else:
            return False
