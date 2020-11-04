from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #不加这两句对全负数list返回0 没通过 要返回最大负数
        if max(nums)<0:
            return max(nums)
        current_sum=0
        #记录下scan到当前位置可能拥有的最大sum ❌这么说不对 应该说记录sum到当前位置可能对后面产生的贡献 sum为正就有贡献 为负就置0从头开始加
        nums_sum=[]
        for i in range(len(nums)):
            #一开始这里写的>0才累积 觉得=0 可以不算 从后面重新开始 但是对nums=[0]的情况 最后的nums_sum为空会调用max失败
            if current_sum+nums[i]>=0:
                current_sum+=nums[i]
            #如果加到当前位置为负数 则不会对后面子串做出贡献 不计入
            else:
                current_sum=0
            nums_sum.append(current_sum)
        return max(nums_sum)

'''执行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了89.86%的用户
内存消耗：
14.8 MB, 在所有 Python3 提交中击败了6.35%的用户'''
