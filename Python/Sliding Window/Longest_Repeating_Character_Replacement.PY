class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen=0
        maxFreq=0
        freq=[0]*26
        l=0
        r=-1
        while r+1<len(s):
            r=r+1
            freq[ord(s[r])-ord('A')]+=1
            maxFreq=max(maxFreq,freq[ord(s[r])-ord('A')])
            while r-l+1-maxFreq>k:
                freq[ord(s[l])-ord('A')]-=1
                l=l+1
            maxLen=max(maxLen,r-l+1)
        return maxLen
