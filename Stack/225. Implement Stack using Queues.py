from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=deque()
        self.helpqueue=deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)



    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while(len(self.queue)>1):
            temp=self.queue.popleft()
            self.helpqueue.append(temp)
        result=self.queue.popleft()
        self.queue,self.helpqueue=self.helpqueue,self.queue
        return result



    def top(self) -> int:
        """
        Get the top element.
        """
        while(len(self.queue)>1):
            temp=self.queue.popleft()
            self.helpqueue.append(temp)
        result=self.queue.popleft()
        self.helpqueue.append(result)
        #忘了吧help置空 就超时了
        self.queue,self.helpqueue=self.helpqueue,self.queue
        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue)==0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


'''执行用时：
44 ms, 在所有 Python3 提交中击败了44.05%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了95.55%的用户'''
