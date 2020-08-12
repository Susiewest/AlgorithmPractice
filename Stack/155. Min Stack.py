class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list=[]

    def push(self, x: int) -> None:
        self.stack_list.append(x)

    def pop(self) -> None:
        pop_element=self.stack_list.pop()
        return pop_element

    def top(self) -> int:
        return self.stack_list[-1]


    def getMin(self) -> int:
        min_element=float('inf')
        for i in range(len(self.stack_list)):
            if self.stack_list[i]<min_element:
                min_element=self.stack_list[i]
        return min_element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



'''执行结果：
通过
执行用时：
4124 ms, 在所有 Python3 提交中击败了5.00%的用户
内存消耗：
16.8 MB, 在所有 Python3 提交中击败了81.67%的用户'''
