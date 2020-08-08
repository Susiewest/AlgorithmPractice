# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #快慢指针碰头法～
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False



'''执行结果：
通过
执行用时：
64 ms, 在所有 Python3 提交中击败了56.59%的用户
内存消耗：
16.8 MB, 在所有 Python3 提交中击败了28.27%的用户'''
