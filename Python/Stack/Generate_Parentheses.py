class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp=[[] for _ in range(n+1)]
        dp[0].append("")
        dp[1].append("()")
        for len in range(2,n+1):
            for leftLen in range (1,len+1):
                insideLen=leftLen-1
                for s in dp[insideLen]:
                    left="("+s+")"
                    rightLen=len-leftLen
                    for x in dp[rightLen]:
                        dp[len].append(left+x)
        return dp[n]

n=int(input())
print(Solution().generateParenthesis(n))