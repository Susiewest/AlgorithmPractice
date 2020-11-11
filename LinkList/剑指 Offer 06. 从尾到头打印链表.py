栈/递归 我的写法算是栈吧，递归的话return内层结果+当前节点的val
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        reverse = []
        pot = head
        while(pot):
            reverse.append(pot.val)
            pot=pot.next
        return reverse[::-1]
        
执行用时：40 ms, 在所有 Python3 提交中击败了94.23%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了46.62%的用户
