class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        tmp=[]
        def backtrack(tmp,depth):
            if depth==len(nums)+1:
                return
            result.append(tmp)
            for i in range(depth,len(nums)):  
                #参数一开始写的depth+1而不是i+1
                #这样写是有问题的 当你depth=0时选了1 
                #depth=1 tmp=[1]时选了3 下一层递归应该从3后开始选择，不能再选2/3了
                #而此时depth+1=2
                #nums[i]从nums[depth](nums[2])开始，也就是又从3开始选 会出现[1,3,3]
                #所以向下层传递的depth应该从当前位置+1，而非depth+1
                backtrack(tmp+[nums[i]],i+1)
        backtrack(tmp,0)
        return result
        
        
        
'''执行用时：
36 ms, 在所有 Python3 提交中击败了88.87%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了5.11%的用户'''
