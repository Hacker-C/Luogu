class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newS=sorted(strs,key=lambda x:len(x))
        if strs==[]:
            return ''
        a=newS[0]
        flag=1
        ans=[]
        for i in range(len(a)):
            for j in range(1,len(strs)):
                if a[i]!=newS[j][i]:
                    flag=0
                    break
            if flag:
                ans.append(a[i])
            else:
                break
        if ans:
            return ''.join(ans)
        else:
            return ""
