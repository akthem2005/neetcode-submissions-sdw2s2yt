class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val: int) -> None:
        if self.stack == []:
            self.mini = [val] 
        elif val<= self.mini[-1]:
            (self.mini).append(val)
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if self.mini[-1] == x:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
