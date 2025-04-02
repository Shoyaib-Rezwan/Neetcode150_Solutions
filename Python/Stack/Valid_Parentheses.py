class stack:
    def __init__(self):
        self.stk=[]
    def push(self,x):
        self.stk.append(x)
    def pop(self):
        if len(self.stk)==0:
            return None
        return self.stk.pop()
    def top(self):
        if len(self.stk)==0:
            return None
        return self.stk[-1]
    def empty(self)->bool:
        return len(self.stk)==0
class Solution:
    def matchBrackets(self,x,y):
        if (x=='(' and y==')') or (x=='{' and y=='}') or (x=='[' and y==']'):
            return True
        return False
    def isValid(self, s: str) -> bool:
        stk=stack()
        for x in s:
            if x=='[' or x=='{' or x=='(':
                stk.push(x)
            else:
                if stk.empty():
                    return False
                top=stk.pop()
                if not self.matchBrackets(top,x):
                    return False
        return True if stk.empty() else False
                

s=input()
print(Solution().isValid(s))