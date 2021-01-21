弱鸡暴力做法。。。
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        result = []
        for i in range(len(nums)-k+1):
            result.append(max(nums[i:i+k]))
        return result

执行用时：476 ms, 在所有 Python3 提交中击败了35.62%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了8.82%的用户

单调栈 实现了随意入栈、出栈情况下的O(1) 时间获取 “栈内最小值” 。 出栈操作” 删除的是 “列表尾部元素” ，而 “窗口滑动” 删除的是 “列表首部元素” 。
所以采用单调队列
错误做法：
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queue = collections.deque()
        result = []
        queue.append(max(nums[0:k]))
        result.append(max(nums[0:k]))
        # 窗口未填满时不能这么写哦，单调队列不一定只保留前三个里面的最大值，还可能保留一个略小一些的值 例子：[9,10,9,-7,-4,-8,2,-6] 5
        for i in range(k,len(nums)):
            if queue and nums[i-k]==queue[0]:
                queue.popleft()
            while queue and queue[-1]<nums[i]:
                queue.pop()
            queue.append(nums[i])
            result.append(queue[0])
        return result
    
    
class Solution:
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    queue = collections.deque()
    result = []
    for i in range(k):
        while queue and queue[-1]<nums[i]:
            queue.pop()
        queue.append(nums[i])
    result.append(queue[0])
    for i in range(k,len(nums)):
        if nums[i-k]==queue[0]:
            queue.popleft()
        while queue and queue[-1]<nums[i]:
            queue.pop()
        queue.append(nums[i])
        result.append(queue[0])
    return result
执行用时：60 ms, 在所有 Python3 提交中击败了93.44%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了18.45%的用户

