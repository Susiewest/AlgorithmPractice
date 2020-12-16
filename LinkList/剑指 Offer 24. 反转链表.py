# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        r = head
        while head:
            r = r.next
            head.next = dummy.next
            dummy.next = head
            head = r
        return dummy.next
执行用时：40 ms, 在所有 Python3 提交中击败了86.16%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了14.01%的用户

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre
            #cur.next = pre 不能先写，先写改变了cur.next就无法递归处理后续链表
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)
执行用时：40 ms, 在所有 Python3 提交中击败了86.16%的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了5.07%的用户

        
