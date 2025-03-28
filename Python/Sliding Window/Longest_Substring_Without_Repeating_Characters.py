class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        freq=[0]*128
        l=0
        r=-1
        while r+1<len(s):
            if freq[ord(s[r+1])]==0:
                r=r+1
                freq[ord(r)]=1
                maxLen=max(maxLen,r-l+1)
            else:
                while freq[ord(s[r+1])]>0:
                    freq[ord(s[l])]=0
                    l=l+1
        return maxLen
    
s=input()
print(Solution().lengthOfLongestSubstring(s))
