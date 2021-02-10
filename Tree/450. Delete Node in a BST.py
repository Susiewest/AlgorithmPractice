时间复杂度O(height of tree)
错误写法，只能将顶替值复制到删除节点，但下面的顶替节点无法正确删除。 [5,3,6,2,4,null,7]，3-->结果应该是[5,2,6,null,4,null,7]，却是[5,2,6,2,4,null,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find_predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def find_successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        p = root
        while p and p.val != key:
            if p.val > key:
                p = p.left
            else:
                p = p.right
        if p:
            if not (p.left or p.right):
                p = None
            elif p.left:
                p.val = self.find_predecessor(p)
                self.deleteNode(p.left, p.val)
            else:
                p.val = self.find_successor(p)
                self.deleteNode(p.right, p.val)
        return root
a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(None)
g = TreeNode(7)
a.left = b
a.right = c
b.left =d
b.right = e
c.left = f
c.right = g
sol = Solution()
ans=sol.deleteNode(a,3)
print(ans)

其实没有完全明白上面为什么错，p = none这步成功的执行了，但却没有修改树本身 p.val却成功的修改了树本身

如果说一层循环只能处理当前root，不能用while的写法利用p找到要删除的节点，然后处理完再返回root。
那么就只处理root的办法是以下写法。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def find_successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val>key:
            root.left = self.deleteNode(root.left, key)。#1
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)。#1
        else:
            if not (root.left or root.right):
                root = None
            elif root.left:
                root.val = self.find_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)。 #2
            else:
                root.val = self.find_successor(root)
                root.right = self.deleteNode(root.right, root.val)。#2
        return root
    
    1/2处的root.left = 和root.right = 都不能省略
执行用时：88 ms, 在所有 Python3 提交中击败了39.32%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了13.55%的用户


