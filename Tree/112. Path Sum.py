# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None and root.val==sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)


'''执行结果：
通过
执行用时：
52 ms, 在所有 Python3 提交中击败了83.76%的用户
内存消耗：
15.6 MB, 在所有 Python3 提交中击败了41.36%的用户'''


#第一次学到队列可以以[a，a.val]的一个元素的形式append 一对值
#思路是用队列bfs存【当前节点，节点值+父节点保存的path的和（即抵达当前节点的path sum）】
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root==None:
            return False
        path=collections.deque()
        path.append([root,root.val])
        while(path):
            node,path_sum=path.popleft()
            if node.left==None and node.right==None and path_sum==sum:
                return True
            if node.left:
                path.append([node.left,path_sum+node.left.val])
            if node.right:
                path.append([node.right,path_sum+node.right.val])
        return False



‘’‘运行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了98.35%的用户
内存消耗：
15.5 MB, 在所有 Python3 提交中击败了70.91%的用户‘’‘
