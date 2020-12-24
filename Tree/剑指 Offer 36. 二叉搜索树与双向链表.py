下面写法是有问题的，dfs函数里对pre和head的修改没有传递到函数外，有点奇怪
按理说我是在函数外定义的pre，head，应该可以在dfs内做修改呀
现在只能委曲求全，给两位大哥加上self.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        pre, head = None, None
        def dfs(pre, head, node):
            if not node: return 
            dfs(pre, head, node.left)
            if pre:
                node.left, pre.right = pre, node
            else:
                head = node #标记头节点
            pre = node
            dfs(pre, head, node.right)
        dfs(pre, head, root)
        pre.right, head.left = head, pre
        return head

增加self版本
思路：首先确定中序遍历，其次必定要保存前后两个节点才能完成双向的指向。
关键在于如何处理头尾节点。
首先中序遍历第一个节点作为头节点，要标记。处理到最后一个节点，尾节点位置也保留，二者再进行最后一步头尾设置。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.pre, self.head = None, None
        def dfs(node):
            if not node: return 
            dfs(node.left)
            if self.pre:
                node.left, self.pre.right = self.pre, node
            else:
                self.head = node #标记头节点
            self.pre = node
            dfs(node.right)
        dfs(root)
        self.pre.right, self.head.left = self.head, self.pre
        return self.head
执行用时：40 ms, 在所有 Python3 提交中击败了90.78%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了5.15%的用户



        
