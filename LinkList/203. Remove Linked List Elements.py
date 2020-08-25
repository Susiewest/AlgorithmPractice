# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #一开始我没有设置point 直接用head写 写到最后发现不知道怎么return整个链表
        #设置了point以后 我又把判断是不是none写在开头 
        #这样发现 [1]除掉=1的以后 会return[1] 应该return[]
        #因为head还是指向第一个节点的 没有办法处理第一个节点
        #所以先处理第一个节点和要除去的数相等的情况，也就是用head=head.next操作找到真正的第一个节点
        #这个时候再判断是不是空 空的直接返回
        #再从这个节点开始利用point往后删除等于val的
        while(head and head.val==val):
            head=head.next
        if head==None: return head
        point=head
        while(point):
            if point.val!=val:
                pre=point
                point=point.next
            else:
                point=point.next
                pre.next=point
        return head


'''执行用时：
68 ms, 在所有 Python3 提交中击败了95.78%的用户
内存消耗：
16.7 MB, 在所有 Python3 提交中击败了75.26%的用户'''
