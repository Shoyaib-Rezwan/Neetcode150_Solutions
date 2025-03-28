def getIndex(x:str)->int:
    return ord(x)-ord('a')
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq=[0]*26
        for x in s1:
            freq[getIndex(x)]+=1
        strlen=0
        l=0
        r=0
        temp=[0]*26
        while r<len(s2):
            temp[getIndex(s2[r])]+=1
            if(temp[getIndex(s2[r])]<=freq[getIndex(s2[r])]):
                strlen+=1
            if(r-l+1>len(s1)):
                temp[getIndex(s2[l])]-=1
                if temp[getIndex(s2[l])]<freq[getIndex(s2[l])]:
                    strlen-=1
                l=l+1
            if strlen==len(s1):
                return True
            r=r+1
        return False
s1,s2=input().split()
print(Solution().checkInclusion(s1,s2))