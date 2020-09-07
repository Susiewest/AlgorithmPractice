# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, current = None, head
        while(current):
            nex=current.next
            current.next=pre
            pre=current
            current=nex
        return pre

'''执行用时：
48 ms, 在所有 Python3 提交中击败了54.41%的用户
内存消耗：
14.5 MB, 在所有 Python3 提交中击败了82.16%的用户'''
