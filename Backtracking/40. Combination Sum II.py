有重复数字，每个只能选一次，目标为target，不能包含重复结果。
有重复数字——排序+设置used
有重复数字+不能包含重复结果——设置used+限制元素选择的起始位置

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        used = [0]*len(candidates)
        self.result = []
        def backtrack(nums, target, start, used, path):
            if target==0:
                self.result.append(path)
                return
            if target<0:
                return
            for i in range(start,len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                    continue
                used[i] = 1
                backtrack(nums, target-nums[i], i+1, used, path+[nums[i]])
                used[i] = 0
        backtrack(candidates, target, 0, used, [])
        return self.result
执行用时：104 ms, 在所有 Python3 提交中击败了26.20%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.01%的用户
