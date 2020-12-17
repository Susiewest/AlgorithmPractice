和21题同，如果用递归办法的话，可以直接对l1,l2操作，不用设置另外的工作指针指向合并位置的前一个位置

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return dummy.next
执行用时：76 ms, 在所有 Python3 提交中击败了14.42%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了8.61%的用户

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val<=l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
执行用时：64 ms, 在所有 Python3 提交中击败了54.18%的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了5.10%的用户

