#比102题增加了27-30行
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        flag=False
        queue=collections.deque()
        result=[]
        queue.append(root)
        while(queue):
            tmp=[]
            curlevel_nodes=len(queue)
            for i in range(curlevel_nodes):
                cur=queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if flag:  
                tmp=tmp[::-1]
            result.append(tmp)
            flag=True if not flag else False            
        return result
执行用时：40 ms, 在所有 Python3 提交中击败了76.46%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了23.11%的用户
