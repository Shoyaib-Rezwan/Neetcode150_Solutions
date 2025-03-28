class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a={nums[0]:0}
        for i in range(1,len(nums)):
            if target - nums[i] in a:
                return [a[target-nums[i]],i]
            a[nums[i]]=i
        return [-1,-1]
n=int(input())
nums=list(map(int,input().split()))
target=int(input())
print(Solution().twoSum(nums,target))