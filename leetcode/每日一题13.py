class Solution:
    def romanToInt(self, s: str) -> int:
        base = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        temp={
            'a':1,
            'b':5,
            'c':10,
            'd':50,
            'e':100,
            'f':500,
            'g':1000,
            'h':4,
            'i':9,
            'j':40,
            'k':90,
            'l':400,
            'm':900
        }
        baseKeys=list(base.keys())
        tempKeys=list(temp.keys())
        ans=0
        for i in range(12, -1, -1):
            s=s.replace(baseKeys[i], tempKeys[i])
        for i in s:
            ans+=temp[i]
        return ans

if __name__ == '__main__':
    a = Solution()
    palindrome_bool = a.romanToInt("III")
    print(palindrome_bool)  
