# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#一个队列实现结点的层次遍历 一个列表存队列里pop出来的结点的val 列表只保留当前层的val 统一append到最终结果列表traversal里 然后清空
#感觉存一个字典 层数：结点值集合 也可以
#看到别人的解法也是建立了三个空间 区别是让队列保存字典 层数：结点 设置一个current_layer记录层数 这样每次current_layer如果都在queue[0]就说明这层还没结束 
#但我的方法是 每次处理当前层结点前 队列中只有当前层的结点 这时计算队列长度来限制处理次数 结束次数再把这一行都append到最终结果里 
#关键在于如何确保lists中的list里是一整行的结点 不多也不少的加入最终output

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traversal=[]
        if root==None:
            return traversal
        temp=collections.deque()
        temp.append(root)
        while(temp):
            cur=[]
            for i in range(len(temp)):
                node=temp.popleft()
                cur.append(node.val)
                #其实光上面两行就足够把目前层的结点都加入了 但还要下面几行处理下一层做准备
                if node.left!=None:
                    temp.append(node.left)
                if node.right!=None:
                    temp.append(node.right)
            traversal.append(cur)
        return traversal[::-1]
        
#一个手写的测试用例    
a = [TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)]
a[0].left = a[1]
a[0].right = a[2]
a[2].left = a[3]
a[2].right = a[4]
root = a[0]

sol = Solution()
res = sol.levelOrderBottom(root)
print(res)



'''Runtime: 44 ms, faster than 47.05% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.3 MB, less than 22.88% of Python3 online submissions for Binary Tree Level Order Traversal II.'''
