后序迭代遍历，设置一个prev，指向当前遍历过的最后一个节点。
每个节点可能进行多次出栈入栈。 如果是第一次出，那就放回去，遍历下右边。如果是第二次出（即prev=右孩子），或者无右孩子，就该当前节点加入result咯！
其中更新prev的地方要特别注意。prev就等于当前加入result的节点。以及当前节点要进行更新！！这里格外重要 root=None
如果不更新，就会继续执行while，向左边深度遍历，死循环。更新为none则不会执行向左的while，而是继续向上pop()。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or prev == root.right:
                result.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return result

执行用时：40 ms, 在所有 Python3 提交中击败了57.75%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.41%的用户


另一个思路，前序遍历 中-左-右。后序遍历左-右-中。于是按照前序遍历写中-右-左，颠倒下左右顺序。然后将结果进行反转。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        prev = None
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            root = stack.pop()
            root = root.left
        return result[::-1]
执行用时：32 ms, 在所有 Python3 提交中击败了94.41%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了15.31%的用户

