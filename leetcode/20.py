class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        flag=1
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop(-1)
                if i==")" and top=="(":
                    flag=1
                elif i=="]" and top=="[":
                    flag=1
                elif i=="}" and top=="{":
                    flag=1
                else:
                    flag=0
            if not flag:
                break
        if flag and (not stack):
            return True
        else:
            return False
