class Solution:

    def encode(self, strs: list[str]) -> str:
        s=""
        for x in strs:
            s+=str(len(x))+'#'+x
        return s
    def decode(self, s: str) -> list[str]:
        strs=[]
        i=0
        while i < len(s):
            num=""
            while(True):
                num+=s[i]
                i=i+1
                if s[i]=='#':
                    break
            num=int(num)
            x=""
            i=i+1
            while num>0:
                x+=s[i]
                i=i+1
                num=num-1
            strs.append(x)
        return strs

strs=input().split()
print(strs)
s=Solution().encode(strs)
print(s)
print(Solution().decode(s))
