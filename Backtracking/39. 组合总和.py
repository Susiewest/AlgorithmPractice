#这个写法没有避免重复
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return []
        candidates.sort()
        result=[]
        path=[]
        def dfs(target,path):
            if target==0:
                result.append(path)
                return
            elif target<0:
                return
            for i in range(len(candidates)):
                dfs(target-candidates[i],path+[candidates[i]])
        dfs(target,path)
        return result
        
 
 #增加了一个参数start避免重复，每次dfs的时候 不再选择之前走到头的路线分支
 #举例子 target=7 先选了2 遍历了所有和为5的组合 下次选了3为起点，子树不会再选2，因为已经包含了3+其他=5的解
 class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return []
        candidates.sort()
        result=[]
        path=[]
        def dfs(start,target,path):
            if target==0:
                result.append(path)
                return
            elif target<0:
                return
            for i in range(start,len(candidates)):
                #[1, 2] + [3] 语法生成了新的列表，没有改变原始的[1,2]所以不需要回溯的部分
                dfs(i,target-candidates[i],path+[candidates[i]])
        dfs(0,target,path)
        return result

'''执行用时：
96 ms, 在所有 Python3 提交中击败了37.92%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了35.28%的用户'''            
            
