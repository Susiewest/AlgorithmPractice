设置一个hash表，保存key和对应node
设置一个双向链表，实现O（1）的删除和插入
为什么不能用单向链表？ 找到了key所在的node 还需要再遍历一边找到他之前的节点，进行删改
为什么链表节点仍需要保留key值，不是已经可以通过hash找到节点了吗？ 删除最久未访问的末尾节点(伪tail的前一个节点）时，要知道该节点的key值，用于去删除哈希表cache里保存的
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #用于映射key到node
        #设置dummy 伪头&尾
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_head(self, key):
        self.cache[key].pre.next=self.cache[key].next
        self.cache[key].next.pre=self.cache[key].pre
        self.cache[key].next=self.head.next
        self.head.next=self.cache[key]
        self.cache[key].next.pre=self.cache[key]
        self.cache[key].pre=self.head

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            #挪动到表头
            self.move_to_head(key)
            #*******题目说的return key 测试用例又要return value*******
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            #*******一开始写的=self.value 这里自己函数的参数不用写self
            self.cache[key].value=value
            #挪动到表头
            self.move_to_head(key)
        else:
            #表里没有，cache又满了，替换表尾节点&去掉cache里的hash，挪到表头
            if len(self.cache)==self.capacity:
                self.cache.pop(self.tail.pre.key) #删除了键值
                #self.cache[self.tail.pre.key].key=key 键值不能直接修改
                self.cache[key]=self.tail.pre
                self.tail.pre.key=key
                self.tail.pre.value=value
                self.move_to_head(key)            
            #增加新节点在伪表头之后      
            else:
                newnode=ListNode(key, value)
                self.cache[key]=newnode
                newnode.next=self.head.next      
                self.head.next=newnode
                newnode.next.pre=newnode
                newnode.pre=self.head



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

执行用时：248 ms, 在所有 Python3 提交中击败了49.90%的用户
内存消耗：22 MB, 在所有 Python3 提交中击败了46.96%的用户
