class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while(len(self.stack1)>1):
            temp=self.stack1.pop()
            self.stack2.append(temp)
        result=self.stack1.pop()
        while(len(self.stack2)>0):
            self.stack1.append(self.stack2.pop())
        #有点问题 这题是双栈实现队列 之前双队列实现栈好像是这么写的 后面可以放一起再做一遍总结下
        #self.stack1, self.stack2=self.stack2, self.stack1
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        while(len(self.stack1)>1):
            temp=self.stack1.pop()
            self.stack2.append(temp)
        result=self.stack1.pop()
        self.stack2.append(result)
        while(len(self.stack2)>0):
            self.stack1.append(self.stack2.pop())
        return result



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.stack1)==0 else False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''执行用时：
36 ms, 在所有 Python3 提交中击败了88.00%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了24.22%的用户'''
