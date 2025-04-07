class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n=len(position)
        cars=[]
        for i in range(n):
            cars.append((position[i],speed[i]))
        cars.sort()
        times=[]
        for x in cars:
            times.append((target-x[0])/x[1])
        stack=[]
        for i in range(n):
            while(len(stack)>0 and times[stack[-1]]<=times[i]):
                stack.pop()
            stack.append(i)
        return len(stack)
n=int(input())
target=int(input())
position=list(map(int,input().split()))
speed=list(map(int,input().split()))
print(Solution().carFleet(target,position,speed))