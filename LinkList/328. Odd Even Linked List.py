dummy1作为奇数链的头 dummy2作为偶数链的头

从head开始遍历，依次轮流附在奇、偶链的后面

遍历完后，奇数链的尾连向偶链的头，偶链的尾为空， 返回奇数链的头

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        dummy1.next = head
        pre, ano = dummy1.next, dummy2
        #true/1: even false/0:odd
        while pre and pre.next:
            head = pre.next
            pre.next = head.next
            ano.next = head
            ano = ano.next 
            ano.next = None #cycle错误      
            if pre.next:
                pre = pre.next     
        if pre:
            pre.next = dummy2.next
        return dummy1.next
            

执行用时：48 ms, 在所有 Python3 提交中击败了86.74%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了73.51%的用户

上面的解法有太多琐碎的冗余了，设置了pre，head做奇数链的工作指针，设置了ano做偶数链的工作指针，还有两个指向头部的dummy
太繁琐
下面的做法 省去了dummy， 头节点是没有变动的，可以不用设置dummy直接指向头部。
不用去维护dummy链表的尾指针 只需在链表上操作

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        # dummy1 = ListNode(-1)
        # dummy2 = ListNode(-1)
        odd = head
        even = head.next
        pre, ano = head, head.next
        #pre指向奇数节点 ano指向偶数节点 ano是偶数链的工作指针
        while ano and ano.next:
            pre.next = ano.next
            ano.next = ano.next.next  
            pre = pre.next
            ano = ano.next       
        pre.next = even
        return odd
    
执行用时：44 ms, 在所有 Python3 提交中击败了95.41%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了26.95%的用户
