首先读完题以为要自己实现next函数里面的if .hasnext(): return 下一个
后来发现大片的注释里最后几行已经完成了这一步
也就是说next函数只需返回下一个即可
这样一次只返回一个，需要递归/迭代处理了当前元素以后再重新加入的，使用栈比较合适（看答案倒推的思路。。
为什么判断和处理都写在hasnext里而不写在next里，我感觉是hasnext首先是执行next前的判断，在这里处理不会对结果造成影响
再就是hasnext既判断了有无下一个，可以顺便把下一个处理好。。我在说什么啊啊啊我这个题其实是没完全想明白的呜呜呜
明天我将尝试使用普通的list，或者说队列（先进的integer先出）来尝试做一下这个题,这样不用全部先倒序存进去，每次pop一个处理完再放回去，而是处理好一个才放进去
下面是看答案写的栈的做法：栈顶元素为整数时，next 函数直接返回
栈顶元素为列表时，hasNext 函数将该列表弹出栈后，再逆序连接（用+而非append）入栈中
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

#首先我是设置了一个空的队列，等nestedlist里处理好了再放进来，这样有一个问题是，迭代处理好了第一个元素以后，无法将指针指向nestedlist的下个元素
#如果设置一个指针指向nestedlist，又无法对刚取出来的元素迭代处理，处理好了一层加入到queue里，里面的层还要继续处理，指针怎么再跳到queue里处理，很乱
#于是我选择了将nestedlist直接复制到queue，然后从第一个元素开始处理
#又出现了问题，不能像栈一样直接“+”了，直接+的话，[]是去掉了，但是元素顺序也变了，处理好的当前元素们应该从队列左端送入
#改为self.queue=self.queue.popleft().getList()+self.queue 又说不能让deque和list concatenate
#无语凝噎 人果然只有在做了尝试以后才知道为什么最好用栈而非队列，栈处理好了直接push进去就好了，队列处理好了还要从头部塞进去
#除非按照最初的想法，不一下子复制过来，处理好一个放一个，但是这样指针又很混乱 日了
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
        self.queue = collections.deque()
        
    
    def next(self) -> int:
        return self.queue.popleft()
        
    
    def hasNext(self) -> bool:
        if len(self.queue)==0:
            if self.queue[0].getInteger():
                self.queue.append(self.nestedList.getInteger())
            else:
                self.queue.append(self.nestedList.getList())
        while len(self.queue)>0 and not self.queue[0].getInteger():
            self.queue=self.queue.popleft().getList()+self.queue #连接两个list
            #这个时候该怎么让nestedlist里面的指针++？
        return len(self.queue)>0
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#不能像栈一样直接“+”了，处理好的当前元素们应该从队列左端送入
#我还是太弱鸡了 日了上面这句话是错的，其实是可以在后面+的，把nestedlist赋值给queue，每次popleft一个，处理好了放在后面，所有的处理完了还是按顺序的
#脑子里一直想着递归，上面的写法在实现的时候又卡了
最后还是看了题解区的队列做法 我好笨呐 也不难 就写不出来呜呜

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
        self.queue = collections.deque()
        def nested(nested_list):
            for i in nested_list:
                #if i.getInteger(): 这么写当interger是0的时候也不执行这个
                if i.isInteger():
                    self.queue.append(i.getInteger())
                else:
                    nested(i.getList())
            #这个时候该怎么让nestedlist里面的指针++？
        nested(nestedList)
    
    def next(self) -> int:
        return self.queue.popleft()
        
    
    def hasNext(self) -> bool:
        # if len(self.queue)==0:
        #     if self.queue[0].getInteger():
        #         self.queue.append(self.nestedList.getInteger())
        #     else:
        #         self.queue.append(self.nestedList.getList())
        return len(self.queue)>0
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

执行用时：72 ms, 在所有 Python3 提交中击败了81.80%的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了33.03%的用户
