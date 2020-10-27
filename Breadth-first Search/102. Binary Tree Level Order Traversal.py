#一口气流畅的写完 自我陶醉觉得写的很好 结果超时 找了很久bug
#发现每次pop出来的存在了cur里，判断应该判断cur的左节点和右节点，而我仍然写root.left root.right
#无语 我不超时谁超时！！！！！！！你知道错了吗！你错在哪了！！！
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue=collections.deque()
        result=[]
        tmp=[]
        queue.append(root)
        tmp.append(root.val)
        while(queue):
            result.append(tmp)
            tmp=[]
            curlevel_nodes=len(queue)
            while(curlevel_nodes):
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    tmp.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    tmp.append(cur.right.val)
                curlevel_nodes-=1
        return result
执行用时：56 ms, 在所有 Python3 提交中击败了9.33%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了17.29%的用户
        
 #上面版本有个缺点 代码27-31行冗余，有更好的方式
 #现在的思路是 每次辅助数组都要append当前节点的左子和右子的值，要写两次，可以转换为 每次pop出来cur的时候，把cur的值append，这样就只用写一次！
 #就是层次遍历的时候，确实queue是要append左子和右子，但是这个题我为了返回的是节点的值，而非节点本身，我同时设置了辅助数组tmp，tmp要和queue同时append，就每个多写了一行
 #其实tmp可以保存cur的值，而非cur左子右子的值，跑到最后也可以实现相同功能
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue=collections.deque()
        result=[]
        queue.append(root)
        #tmp.append(root.val)
        while(queue):
            tmp=[]
            curlevel_nodes=len(queue)
            for i in range(curlevel_nodes):
                cur=queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                    #tmp.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    #tmp.append(cur.right.val)
            result.append(tmp)            
        return result
执行用时：44 ms, 在所有 Python3 提交中击败了62.73%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了84.83%的用户

 
