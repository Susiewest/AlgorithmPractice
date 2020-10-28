# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, preleft, preright, inorder,inleft,inright):
            #忘了写终止条件
            if(preleft>preright or inleft>inright):
                return None
            root=TreeNode(preorder[preleft])
            in_root=chart[preorder[preleft]]
            nodes_left=in_root-inleft
            root.left=build(preorder,preleft+1,preleft+nodes_left,inorder,inleft,in_root-1)
            root.right=build(preorder,preleft+nodes_left+1,preright,inorder,in_root+1,inright)    
            #一开始没写这句 啥也没return 要把下层构建好的树return到上层挂在孩子上
            return root
        presize=len(preorder)
        insize=len(inorder)
        if presize!=insize:
            return None
        #还能这么写！抄到了！（
        #为了不每次重定位 对inorder生成一个哈希键值对
        chart={element:i for i,element in enumerate(inorder)}
        return build(preorder, 0, presize-1, inorder,0,insize-1)
        
执行用时：60 ms, 在所有 Python3 提交中击败了81.06%的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了69.65%的用户

#把无用参数去掉了 inorder是完全可以去掉的 因为有了hash表不需要inorder了 preorder可以保留但我也去了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preleft, preright,inleft,inright):
            #忘了写终止条件
            if(preleft>preright or inleft>inright):
                return None
            root=TreeNode(preorder[preleft])
            in_root=chart[preorder[preleft]]
            nodes_left=in_root-inleft
            root.left=build(preleft+1,preleft+nodes_left,inleft,in_root-1)
            root.right=build(preleft+nodes_left+1,preright,in_root+1,inright)    
            #一开始没写这句 啥也没return 要把下层构建好的树return到上层挂在孩子上
            return root
        presize=len(preorder)
        insize=len(inorder)
        if presize!=insize:
            return None
        #还能这么写！抄到了！（
        chart={element:i for i,element in enumerate(inorder)}
        return build(0, presize-1,0,insize-1)
  
执行用时：36 ms, 在所有 Python3 提交中击败了99.83%的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了67.48%的用户


上个方法是用绝对下标写，这个是相对下标，所以每次取in_root要重定位，而非用固定下标
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder,inorder):
            #忘了写终止条件
            if not (preorder and inorder):
                return None
            root=TreeNode(preorder[0])
            #in_root=chart[preorder[0]] 这样写不行 这样下标是固定的了 而非随着函数参数变化而变化的
            in_root=inorder.index(preorder[0])
            root.left=build(preorder[1:in_root+1],inorder[0:in_root])
            root.right=build(preorder[in_root+1:],inorder[in_root+1:])    
            #一开始没写这句 啥也没return 要把下层构建好的树return到上层挂在孩子上
            return root
        return build(preorder,inorder)
执行用时：196 ms, 在所有 Python3 提交中击败了47.58%的用户
内存消耗：86.5 MB, 在所有 Python3 提交中击败了5.05%的用户
