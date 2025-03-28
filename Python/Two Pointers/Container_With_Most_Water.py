class Solution:
    def maxArea(self, heights: list[int]) -> int:
        area=0
        i=0
        j=len(heights)-1
        while i<j:
            if heights[i]<heights[j]:
                area=max(area,heights[i]*(j-i))
                i+=1
            else:
                area=max(area,heights[j]*(j-i))
                j-=1
        return area
n=int(input())
heights=list(map(int,input().split()))
print(Solution().maxArea(heights))