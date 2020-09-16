#妙啊 这题一开始没看出来是bst 二叉搜索树
#左边值小右边值大 根据结点值就可以判断pq在哪边子树
#这样子其实也不需要回溯 所以可以考虑迭代 代替递归 节省空间复杂度 时间复杂度二者都是o（n）（看的答案这么说

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val:
            #忘了写return。。递归要写return的
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

'''执行用时：
92 ms, 在所有 Python3 提交中击败了89.06%的用户
内存消耗：
17.3 MB, 在所有 Python3 提交中击败了80.22%的用户'''         
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#一开始这么写 测试用例总是有两个过不去
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while(root):
            if p.val<root.val and q.val<root.val:
            #忘了写return。。递归要写return的
                root=root.left
            if p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root
#对比答案后加了最后一句话
        return root
        #之前的递归写法 哪怕是空也会返回空结点本身 但这里的迭代判断条件是不为空 为空的话没有返回值 很那个

'''执行用时：
96 ms, 在所有 Python3 提交中击败了76.02%的用户
内存消耗：
17.1 MB, 在所有 Python3 提交中击败了97.37%的用户'''

#md又很迷。。我把最后一句删了又不报错了。。。
'''执行用时：
76 ms, 在所有 Python3 提交中击败了99.97%的用户
内存消耗：
17.4 MB, 在所有 Python3 提交中击败了54.50%的用户'''

       
 
