class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        currentMin=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            maxProfit=max(maxProfit,prices[i]-currentMin)
            currentMin=min(currentMin,prices[i])
        return maxProfit

n=int(input())
prices=list(map(int,input().split()))
print(Solution().maxProfit(prices))