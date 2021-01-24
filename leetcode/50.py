class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        m=n
        if n<0:
            n=-n
        while n!=0:
            if n%2==1:
                ans*=x
            x*=x
            n//=2
        return ans if m>0 else 1/ans
a=Solution()
print(a.myPow(2.0,-2))
