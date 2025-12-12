class MyQueue:

    def __init__(self):
        self.stack=list()

    def push(self, x: int) -> None:
        self.stack.insert(0,x)

    def pop(self) -> int:
        element=self.stack.pop()
        return element
        
    def peek(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()