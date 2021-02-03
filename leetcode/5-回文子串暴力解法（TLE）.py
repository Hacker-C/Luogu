class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)

        def tenet(x):
            if ''.join(list(reversed(x)))==x:
                return 1
            return 0

        maxl=1
        ans=s[0]
        for i in range(l):
            for j in range(i+1,l+1):
                subs=''.join(s[i:j])
                if tenet(subs) and len(subs)>maxl:
                    maxl=len(subs)
                    ans=subs
        return ans
