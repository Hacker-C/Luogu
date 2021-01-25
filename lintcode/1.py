class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        while b!=0:
            xor = a^b
            conj=(a&b)<<1
            a=xor
            b=conj
        return a
a=Solution()
ans=a.aplusb(900,-299)
print(ans)
