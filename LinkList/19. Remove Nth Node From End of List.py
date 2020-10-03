#第一次不看答案做中等题可以达到这么高的击败率！！！好开心呀
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        goFirst, goLater=head, head
        for i in range(n):
            goFirst=goFirst.next
        if goFirst==None:
            return head.next        
        while(goFirst.next):
            goFirst=goFirst.next
            goLater=goLater.next
        goLater.next=goLater.next.next
        return head
'''执行用时：
24 ms, 在所有 Python3 提交中击败了99.94%的用户
内存消耗：
13.2 MB, 在所有 Python3 提交中击败了91.89%的用户'''
