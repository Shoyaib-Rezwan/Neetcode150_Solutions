class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        nge=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if(len(stack)!=0 and temperatures[stack[-1]]>temperatures[i]):
                nge[i]=stack[-1]-i
            else:
                while(len(stack)>1 and temperatures[stack[-1]]<=temperatures[i]):
                    stack.pop()
                if len(stack)!=0:
                    nge[i]=stack[-1]-i
            stack.append(i)
        return nge