class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s=set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False
n=int(input())
nums=list(map(int,input().split()))
obj=Solution()
print(obj.hasDuplicate(nums))