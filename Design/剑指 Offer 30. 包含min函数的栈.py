设置辅助栈B保存A中所有非严格降序的元素，则A中的最小元素始终对应栈B的栈顶元素。非严格降序是因为，最小值如果存在两次，pop一次后不能影响下一次的getmin
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helpstack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helpstack or self.helpstack[-1]>=x:
            self.helpstack.append(x)


    def pop(self) -> None:
        if self.stack.pop()==self.helpstack[-1]:
            self.helpstack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.helpstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
执行用时：56 ms, 在所有 Python3 提交中击败了99.04%的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了12.17%的用户

