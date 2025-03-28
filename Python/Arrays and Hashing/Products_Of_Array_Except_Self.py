class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefixProducts=[]
        postfixProducts=[1]*len(nums)
        prefixProducts.append(1)
        for i in range(1,len(nums)):
            prefixProducts.append(prefixProducts[i-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            postfixProducts[i]=postfixProducts[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            prefixProducts[i]=prefixProducts[i]*postfixProducts[i]
        return prefixProducts
n=int(input())
nums=list(map(int,input().split()))
print(Solution().productExceptSelf(nums))