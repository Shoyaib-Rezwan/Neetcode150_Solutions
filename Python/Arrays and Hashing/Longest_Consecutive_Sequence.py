class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        maxSeq=1
        i=1
        while i<len(nums):
            currSeq=1
            while i<len(nums) and nums[i]<=nums[i-1]+1:
                if nums[i]==nums[i-1]+1:
                    currSeq+=1
                i=i+1
            maxSeq=max(maxSeq,currSeq)
            i=i+1
        return maxSeq
n=int(input())
nums=list(map(int,input().split()))
print(Solution().longestConsecutive(nums))