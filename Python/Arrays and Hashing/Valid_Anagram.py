class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for x in s:
            freq[ord(x)-ord('a')]+=1
        for x in t:
            freq[ord(x)-ord('a')]-=1
        for x in freq:
            if x!=0:
                return False
        return True
s,t=input().split()
print(Solution().isAnagram(s,t))