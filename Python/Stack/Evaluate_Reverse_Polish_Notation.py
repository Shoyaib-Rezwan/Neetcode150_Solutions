class stack:
    def __init__(self):
        self.s=[]
    def push(self,val)->None:
        self.s.append(val)
    def pop(self)->int:
        if len(self.s)==0:
            return None
        return self.s.pop()
def isOperator(x:str)->bool:
    return x=='+' or x=='-' or x=='*' or x=='/'
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk=stack()
        for s in tokens:
            if not isOperator(s):
                stk.push(int(s))
            else:
                b=stk.pop()
                a=stk.pop()
                c=0
                if s=='+':
                    c=a+b
                elif s=='-':
                    c=a-b
                elif s=='*':
                    c=a*b
                else:
                    c=int(a/b)
                stk.push(c)
        return stk.pop()
tokens=input().split()
print(Solution().evalRPN(tokens))    
