class MyQueue:

    def __init__(self):
        self.readStack = []
        self.writeStack = []
        
    def push(self, x: int) -> None:
        self.readStack.append(x)

    def pop(self) -> int:
        if not self.writeStack:
            while self.readStack:
                self.writeStack.append(self.readStack.pop())
        return self.writeStack.pop()

    def peek(self) -> int:
        if not self.writeStack:
            while self.readStack:
                self.writeStack.append(self.readStack.pop())
        return self.writeStack[-1]

    def empty(self) -> bool:
        return max(len(self.readStack), len(self.writeStack)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
