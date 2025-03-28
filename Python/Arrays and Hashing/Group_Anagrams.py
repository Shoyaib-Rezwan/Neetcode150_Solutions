def calculateFreqArray(s:str)->list[int]:
    freq=[0]*26
    for x in s:
        freq[ord(x)-ord('a')]+=1
    return freq
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp={}
        for s in strs:
            freq=tuple(calculateFreqArray(s))
            if freq in mp:
                mp[freq].append(s)
            else:
                mp[freq]=[s]
        result=[]
        for x in mp:
            result.append(mp[x])
        return result

strs=input().split()
print(Solution().groupAnagrams(strs))            