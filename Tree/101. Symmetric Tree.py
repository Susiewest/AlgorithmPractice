#递归方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        def isSym(subroot1,subroot2):
            if subroot1==None and subroot2==None:
                return True
            if subroot1==None or subroot2==None:
                return False
            if subroot1.val==subroot2.val:
                #return self.isSym(subroot1.left,subroot2.right) and self.isSym(subroot1.right,subroot2.left) 
                return isSym(subroot1.left,subroot2.right) and isSym(subroot1.right,subroot2.left) 

        return isSym(root.left,root.right)

  
  
  '''Runtime: 40 ms, faster than 43.20% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 72.36% of Python3 online submissions for Symmetric Tree.'''





#队列方法
'''，collections.deque在数据结构层面实现了队列，但是并没有应用场景方面的支持，可以看做是一个基础的数据结构。
queue模块实现了面向多生产线程、多消费线程的队列，asyncio.queue模块则实现了面向多生产协程、多消费协程的队列，而multiprocessing.queue模块实现了面向多成产进程、多消费进程的队列。'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        #sym=[]
        sym=collections.deque()
        sym.append(root)
        sym.append(root)
        while(len(sym)>0):
            left, right= sym.popleft(),sym.popleft()
            if left==None and right==None:
                #这里不能像递归一样return true 递归只是返回上层 这里return了就直接结束了
                continue
            if left==None or right==None or left.val!=right.val:
                return False
            if left.val==right.val:
                sym.append(left.left)
                sym.append(right.right)
                sym.append(left.right)
                sym.append(right.left)
        return True

   
   '''Runtime: 36 ms, faster than 68.03% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 85.73% of Python3 online submissions for Symmetric Tree.'''
