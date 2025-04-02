class MinStack:

    def __init__(self):
        self.s=[]
        self.temp=[]
    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.temp)==0 or self.temp[-1]>=val:
            self.temp.append(val)
        else:
            self.temp.append(self.temp[-1])

    def pop(self) -> None:
        if len(self.s)==0:
            return None
        self.s.pop()
        self.temp.pop()

    def top(self) -> int:
        if len(self.s)==0:
            return None
        return self.s[-1]

    def getMin(self) -> int:
        if len(self.s)==0:
            return None
        return self.temp[-1]
    