class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp={}
        for x in nums:
            if x in mp:
                mp[x]+=1
            else:
                mp[x]=0
        bucket=[[] for _ in range(len(nums)+1)]
        for x in mp:
            bucket[mp[x]].append(x)
        result=[]
        for i in range(len(nums),0,-1):
            for x in bucket[i]:
                result.append(x)
                k-=1
                if k==0:
                    return result
        return result
n=int(input())
nums=list(map(int,input().split()))
k=int(input())
print(Solution().topKFrequent(nums,k))