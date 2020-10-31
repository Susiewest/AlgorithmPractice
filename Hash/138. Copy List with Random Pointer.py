如果没有random，直接复制过来就完事了，但是由于有random，它会随机指向下一个，但是如果此时被随机指向的那个节点还没有生成，就无法指向。
所以先利用哈希表把所有节点先拷贝一遍，然后在挨个取出来连接一下。
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #1. 复制节点 建立哈希
        #2. 遍历原链表 同时把克隆人对应着连上
        if not head:
            return None
        p=head
        hashmap={}
        while(p):
            copy=Node(p.val, None, None)
            hashmap[p]=copy
            p=p.next
        p=head
        while(p):
            if p.next:
                hashmap[p].next=hashmap[p.next]
            if p.random:
                hashmap[p].random=hashmap[p.random]
            p=p.next
        return hashmap[head]

执行用时：44 ms, 在所有 Python3 提交中击败了83.27%的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了34.62%的用户

看题解的另一个办法:
        #1. 每个节点身后复制一个克隆人
        #2. 将克隆人们之间连接上
        #3. 分开本人和克隆人，剥离！

