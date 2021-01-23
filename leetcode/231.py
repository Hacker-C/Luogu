class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n>0 and (1<<32)%n==0)
