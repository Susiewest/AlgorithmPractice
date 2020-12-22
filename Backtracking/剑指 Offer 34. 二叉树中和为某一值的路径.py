下面这个做法输出的result，比预期result每个都重复一遍 疑惑
啊！！！我知道了，走到最后一个叶节点，会对叶节点的左孩子和右孩子分别调用backtrack
左右孩子都是空，target都是0，都会加入一遍result！

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def backtrack(root, num_sum, tmp):
            #不能这么写呀 满足条件的路径走到最后，还没加入result就return了
            # if not root:
            #     return
            if num_sum==0 and not root: 
                result.append(tmp)
                return
            if not root:
                return
            if num_sum-root.val>=0:
                backtrack(root.left, num_sum-root.val, tmp+[root.val])
                backtrack(root.right, num_sum-root.val, tmp+[root.val])
            else:
                return
        result = []
        backtrack(root, sum, [])
        return result
        
终于改对了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def backtrack(root, num_sum, tmp):
            if not root:
                return
            之前的写法到达叶子了继续进行左右孩子的下一层循环，下一层都为空，这一条path分别加入result一次，造成了重复
            所以在这里当左右孩子为空且当前节点加入后==0时 直接就加入一次，孩子为空就不加入了直接return
            if num_sum-root.val==0 and not root.left and not root.right: 
                result.append(tmp+[root.val])
                return        
            有测试用例中间就等于0了，后面-1再+1到叶子了还是等于0，所以即使等于0了也不能停止脚步
            
            #if num_sum-root.val!=0:
            backtrack(root.left, num_sum-root.val, tmp+[root.val])
            backtrack(root.right, num_sum-root.val, tmp+[root.val])
            # 本以为小于0就不用继续判断了，没想到还有target=-5的情况
            # else:
            #     return
        result = []
        backtrack(root, sum, [])
        return result
执行用时：40 ms, 在所有 Python3 提交中击败了97.97%的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了5.03%的用户

