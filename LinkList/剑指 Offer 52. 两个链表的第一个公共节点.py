要把none==none的情况保证能够执行while 
否则若无交点会超时
160题写法总结更好

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p1
        
执行用时：164 ms, 在所有 Python3 提交中击败了74.89%的用户
内存消耗：29.4 MB, 在所有 Python3 提交中击败了25.74%的用户
