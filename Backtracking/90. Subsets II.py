子集类型的题目，为了避免[2,1] [1,2]的重复，还是需要限制一下选择当前元素的起始位置。
而不是for i in range（len(nums))全范围扫射加入temp list。

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(used, temp, nums, start):
            self.result.append(temp)
            if len(temp)==len(nums):
                return
            for i in range(start,len(nums)):
                if used[i]==1:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                    continue
                else:
                    used[i] = 1
                    backtrack(used, temp+[nums[i]], nums, i+1)
                    used[i] = 0
        self.result = []
        used = [0]*len(nums)
        nums.sort()
        backtrack(used,[],nums, 0)
        return self.result

        
执行用时：40 ms, 在所有 Python3 提交中击败了78.94%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了79.57%的用户
