# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for i in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
执行用时：44 ms, 在所有 Python3 提交中击败了49.14%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.17%的用户



