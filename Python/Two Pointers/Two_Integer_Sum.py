class Solution:
    def twoSum(self, numbers: list[int], target: int)->list[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if(numbers[i]+numbers[j]==target):
                return[i+1,j+1]
            if numbers[i]+numbers[j]>target:
                j=j-1
            else:
                i=i+1
        return [0,0]
n=int(input())
numbers=list(map(int,input().split()))
target=int(input())
print(Solution().twoSum(numbers,target))