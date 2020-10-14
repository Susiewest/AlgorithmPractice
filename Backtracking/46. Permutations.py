class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        used=[False]*len(nums)
        def dfs(path,depth):
            if depth==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    dfs(path,depth+1)
                    used[i]=False
                    path.pop()
        dfs(path,0)
        return result
        
        
'''执行用时：
44 ms, 在所有 Python3 提交中击败了66.47%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了5.14%的用户'''
