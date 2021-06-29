选择列表每次都是当前temp list里最后一个元素后面的数，不选前面的，这是子集，不是全排列。
全排列的话，[1,2],[2,1]是不一样的，且每个结果要包含所有元素；
子集的话，[1,2],[2,1]是一样的，且每个结果不一定包含所有元素，甚至还有空集。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        tmp=[]
        def backtrack(tmp,depth):
            # 为什么这里要+1呢，因为要把最后一层的结果加入到result里，不然depth==len就return缺少最后一个元素
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


下面这个写法比较舒服，全排列是全包含了才能加入result。而子集在设置好候选list的条件下，每个中间结果都可以加入result。
所以result.append()的位置比46 47题有些许变动

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        tmp=[]
        def backtrack(tmp,depth):
            result.append(tmp)
            if depth==len(nums):
                return
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
    
执行用时：36 ms, 在所有 Python3 提交中击败了86.00%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.02%的用户
