"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root:'Node'):
            if root is None or root.left is None:
                return
            root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            dfs(root.left)
            dfs(root.right)
            return root
        #以下写法只是为了处理一个特殊的测试用例 [0]——>[0,#]    
        后来发现这里完全可以不用写！！！！29-30行才是最重要的改变！！！！
        if not root:
            return
        if not root.left:
            root.next=None
        #写return dfs是不对的，[0]的时候还是不会将处理好的root返回 所以分开写
        dfs(root)
        return root
        
执行用时：72 ms, 在所有 Python3 提交中击败了70.83%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了17.58%的用户

本人完美代码，一开始直接在connect里面写递归，这样[0]就直接return了，没有任何返回值，其实root本身应该返回的
而且也不用煞费苦心的让root.next=null 已经是空了，关键在于return root而非给root.next赋值
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root:'Node'):
            if root is None or root.left is None:
                return
            root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            dfs(root.left)
            dfs(root.right)
            return root
        #以下写法只是为了处理一个特殊的测试用例 [0]——>[0,#]
        #写return dfs是不对的，[0]的时候还是不会将处理好的root返回 所以分开写
        dfs(root)
        return root

    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root):
            if root.left is None or root.right is None:
                return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            dfs(root.left)
            dfs(root.right)
            return root
        if root is None:
            return None
        root.next = None
        dfs(root)
        return root
    
执行用时：60 ms, 在所有 Python3 提交中击败了98.30%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了20.53%的用户
