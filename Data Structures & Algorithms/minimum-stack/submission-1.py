class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == []:
            self.mini = [val]
        elif val<=self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.mini[-1]:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.mini)
        return self.mini[-1]
        
