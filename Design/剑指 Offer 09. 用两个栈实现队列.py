class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        #stack2 为空 stack1为空
        if not self.stack1:
            return -1
        #stack1不为空
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

执行用时：552 ms, 在所有 Python3 提交中击败了67.32%的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了6.52%的用户
