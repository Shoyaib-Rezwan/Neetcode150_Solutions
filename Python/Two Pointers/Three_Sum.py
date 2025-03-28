class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets=set()
        for i in range(1,len(nums)-1):
            target=-nums[i]
            j=0
            k=len(nums)-1
            while j<i and k>i:
                if nums[j]+nums[k]==target :
                    triplets.add((nums[j],nums[i],nums[k]))
                    j=j+1
                    k=k-1
                elif nums[j]+nums[k]<target:
                    j=j+1
                else:
                    k=k-1
        result=[]
        for x in triplets:
            result.append(list(x))
        return result
n=int(input())
nums=list(map(int,input().split()))