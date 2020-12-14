# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val==val:
            return head.next
        pre, cur = head, head.next
        while cur.val!=val:
            pre = pre.next
            cur = cur.next
        pre.next=pre.next.next
        return head 
执行用时：36 ms, 在所有 Python3 提交中击败了97.80%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.29%的用户

