def isAlpaNumeric(s:str)->bool:
    if ord(s)>=ord('A') and ord(s)<=ord('Z'):
        return True
    if ord(s)>=ord('a') and ord(s)<=ord('z'):
        return True
    if ord(s)>=ord('0') and ord(s)<=ord('9'):
        return True
    return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if not isAlpaNumeric(s[i]):
                i=i+1
                continue
            if not isAlpaNumeric(s[j]):
                j=j-1
                continue
            if(s[i].upper()!=s[j].upper()):
                return False
            i+=1
            j-=1
        return True
s=input()
print(Solution().isPalindrome(s))