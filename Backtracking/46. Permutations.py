#https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        used=[False]*len(nums)
        def dfs(path,depth):
            if depth==len(nums):
                #这里很重要 一开始append（path） result是[[],[],[],[]]这样的
                #因为path是传址，对象类型变量在传参的过程中，复制的是变量的地址。这些地址被添加到 result 变量，但实际上指向的是同一块内存地址
                #因此最后path回到根节点为[]，所有指向这个地址的都会变成空
                #res.append(path) 把 path 的地址复制到 res 中；
                #res.append(path[:]) 把 path 复制了一份，把新复制的列表的地址复制到 res 中。
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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtrack(nums,temp):
            # if len(temp)==len(nums): 不行啊 不能这么写，nums一直在变的
            if not nums:
                self.result.append(temp)
                # return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],temp+[nums[i]])
        backtrack(nums, [])
        return self.result
执行用时：48 ms, 在所有 Python3 提交中击败了30.65%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.13%的用户

# 写了return
执行用时：48 ms, 在所有 Python3 提交中击败了30.65%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了51.28%的用户
