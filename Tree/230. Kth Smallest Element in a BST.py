中序遍历后return k-1位置
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        def dfs(root: TreeNode):
            if root is None:
                return 
            dfs(root.left)           
            inorder.append(root.val)
            dfs(root.right)
        dfs(root)
        return inorder[k-1]
执行用时：56 ms, 在所有 Python3 提交中击败了92.64%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了60.30%的用户

递归转迭代
迭代写树要包含两层while 一层保证node不为空或stack不为空（若是查找某个位置元素，一定会存在，可以直接写while true，找到了直接return
一层保证工作指针不为空时不断遍历，为空则做某些操作
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = []
        while True:      
            while root:
                inorder.append(root)
                root = root.left  
            root = inorder.pop()
            k-=1
            if k==0:
                return root.val
            root = root.right
执行用时：64 ms, 在所有 Python3 提交中击败了70.60%的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了11.21%的用户

二分查找，如果左子树节点num==k-1 return root.val 否则 小于则去右子树找左子树节点为k-num-1个 大于则去左子树找k
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(root: TreeNode):
            if root is None:
                return 0
            return dfs(root.left)+dfs(root.right)+1
        node_num = dfs(root.left)
        if node_num==k-1:
            return root.val
        if node_num<k-1:
            return self.kthSmallest(root.right, k-node_num-1)
        if node_num>k-1:
            return self.kthSmallest(root.left, k)

执行用时：64 ms, 在所有 Python3 提交中击败了70.60%的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了23.43%的用户
       

               
