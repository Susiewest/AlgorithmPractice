只有在新选择的元素，和上一个被释放的元素相同时，剪枝。
只可能两个1都在/都不在，目前列表中只有一个，且和上一个选过的相同的话就要剪枝掉一种情况。

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(temp, nums, used):
            if len(temp)==len(nums):
                self.result.append(temp)
                return
            for i in range(len(nums)):
                if used[i]==1:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0: #是判断另一个重复的用了没，没用（被撤消了选择），那就别选我，用了，再选我；先选前面的再选我，为了避免两个重复元素里，出现先选它再选我+先选我再选它当成不同的两个结果。
                #如果判断 usedused[i]==0，那就continue的话，永远也没法达到len(temp)==len(nums)
                    continue                               
                used[i] = 1
                # backtrack(temp+nums[i],nums,used)
                backtrack(temp+[nums[i]],nums,used)
                used[i] = 0
        used = [0]*len(nums)
        self.result = []
        nums.sort() # 错误写法 nums=nums.sort()
        backtrack([],nums,used)
        return self.result
        
执行用时：52 ms, 在所有 Python3 提交中击败了67.97%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了15.59%的用户
