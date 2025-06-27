#实现一个stack 数据结构并且时间复杂度要在o(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.getMin() if self.miniStack else val )
        self.miniStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.miniStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]