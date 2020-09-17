# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
        #node=node.next
        #好机智呀 node.next.next其实是指的后面一串？
        #那么为什么不能 node=node.next呢？
        
        
        
'''执行用时：
48 ms, 在所有 Python3 提交中击败了79.49%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了45.09%的用户'''
