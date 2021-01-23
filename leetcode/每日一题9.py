class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y=''.join(reversed(list(x)))
        if x==y:
            return True
        else:
            return False
