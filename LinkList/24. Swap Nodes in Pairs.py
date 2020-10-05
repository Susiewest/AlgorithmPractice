#这一版本的代码有点问题，主要是因为疯狂的使用.next.next 会出现.next为none，none没有next属性的尴尬情况
#那么如何解决这种尴尬情况 我的想法是 把.next.next这步写在下次循环的开头，在while里判断了.next不为空了再.next.next
#我在说什么。。。
#学到的第二个小技巧就是在一通操作以后 head不再是head 那么如何返回整个链表 设置一个空头 return空头.next
#以前考研学数据结构说过 为什么要设置空头 是为了让head的处理方法和后面的节点都一样保持一致 不需另外处理 现在有所领悟了
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #如果经过一番操作 head已不是最初的head 那么可以设置一个空头 dummy
        #return dummy.next
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
	first, second=pre.next, pre.next.next
        while(first and second):
            first.next=second.next
            second.next=first
            pre.next=second
            pre=first
            #如何巧妙避免 none has no attribute ‘next’的报错****
            first, second=pre.next, pre.next.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #如果经过一番操作 head已不是最初的head 那么可以设置一个空头 dummy
        #return dummy.next
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        while(head and head.next):
            first, second=head,head.next
            first.next=second.next
            second.next=first
            pre.next=second
            pre=first
            #如何巧妙避免 none has no attribute ‘next’的报错
            head=first.next
        return dummy.next

‘’’执行用时：44 ms, 在所有 Python3 提交中击败了50.94%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了9.19%的用户‘’’
