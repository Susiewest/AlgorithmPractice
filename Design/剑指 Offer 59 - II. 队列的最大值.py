这种题感觉要搞清楚到底要不要得到值以后pop，还是只需要得到值，值仍在队列里
疑惑：用双端队列只能保证得到最大的top2，比如4203，只保留43，20都被pop出去了，那我第三次取maxvalue取不到2怎么办
解答：20比3先进队列，如果3被pop了，证明20早被pop了，取maxvalue根本取不到20
因此保留当前元素之前的，比当前元素小的元素，根本用不到，因为在pop到当前元素前，较小元素都没意义

class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()
        self.help_queue = collections.deque()

    def max_value(self) -> int:
        return self.help_queue[0] if self.help_queue else -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        #需要从队列尾部取出元素，因此需要使用双端队列来实现
        while self.help_queue and self.help_queue[-1]<value:
            self.help_queue.pop()
        self.help_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        result = self.queue.popleft() 
        if self.help_queue and result == self.help_queue[0]:
            self.help_queue.popleft()
        return result


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
执行用时：256 ms, 在所有 Python3 提交中击败了45.27%的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了10.22%的用户

