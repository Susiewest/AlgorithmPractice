这题比较那啥的一个地方可能就是层次遍历保存的是节点，但是需要return 节点的val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
            
执行用时：44 ms, 在所有 Python3 提交中击败了51.49%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.10%的用户


