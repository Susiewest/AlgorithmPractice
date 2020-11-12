完全自己想的思路&写的题解 find mid-reverse-concate
为什么题解里合并没有考虑l1/l2多一个的情况

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        #find mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second
        p = slow.next #the first node
        #一开始没这句话 报错说listnode里发现了cycle
        slow.next = None
        r = p.next
        dummy = ListNode(-1)
        dummy.next = None
        while p:
            r = p.next
            p.next = dummy.next
            dummy.next = p
            p = r
        result = ListNode(-1)
        #concate head and dummy
        p1 = head
        p2 = dummy.next
        cur = result
        while p1 and p2:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
            cur.next = p2
            p2 = p2.next
            cur = cur.next
        cur.next = p1 or p2
        return result.next

执行用时：108 ms, 在所有 Python3 提交中击败了45.44%的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了48.66%的用户

