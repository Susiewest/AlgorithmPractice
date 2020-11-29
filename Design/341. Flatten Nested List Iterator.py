首先读完题以为要自己实现next函数里面的if .hasnext(): return 下一个
后来发现大片的注释里最后几行已经完成了这一步
也就是说next函数只需返回下一个即可
这样一次只返回一个，需要递归/迭代处理了当前元素以后再重新加入的，使用栈比较合适（看答案倒推的思路。。
为什么判断和处理都写在hasnext里而不写在next里，我感觉是hasnext首先是执行next前的判断，在这里处理不会对结果造成影响
再就是hasnext既判断了有无下一个，可以顺便把下一个处理好。。我在说什么啊啊啊我这个题其实是没完全想明白的呜呜呜
下面我将尝试使用普通的list，或者说队列（先进的integer先出）来尝试做一下这个题,这样不用全部先倒序存进去，每次pop一个处理完再放回去，而是处理好一个才放进去

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        
    
    def next(self) -> int:
        return self.stack.pop()
        
    
    def hasNext(self) -> bool:
        while len(self.stack)>0 and not self.stack[-1].isInteger():
            self.stack+=self.stack.pop().getList()[::-1] #连接两个list
        return len(self.stack)>0
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

执行用时：88 ms, 在所有 Python3 提交中击败了27.13%的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了15.84%的用户

