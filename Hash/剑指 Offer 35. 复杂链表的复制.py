"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        correspond_node = {}
        cur = head
        while cur:
            correspond_node[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                correspond_node[cur].next = correspond_node[cur.next]
            if cur.random:
                correspond_node[cur].random = correspond_node[cur.random]
            cur = cur.next
        return correspond_node[head]
执行用时：36 ms, 在所有 Python3 提交中击败了97.13%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了14.70%的用户

