# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildSubTree(start_idx,end_idx):
            if start_idx>end_idx:
                return None
            mid_idx=(start_idx+end_idx)//2
            root=TreeNode(nums[mid_idx])
            root.left=buildSubTree(start_idx,mid_idx-1)
            root.right=buildSubTree(mid_idx+1,end_idx)
            return root
        #这里不是range也不是数组了不要忘了写-1
        return buildSubTree(0,len(nums)-1)



'''执行结果：
通过
执行用时：
64 ms, 在所有 Python3 提交中击败了40.53%的用户
内存消耗：
16 MB, 在所有 Python3 提交中击败了12.50%的用户'''
