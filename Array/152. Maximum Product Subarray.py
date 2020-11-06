非传统型滑动窗口
如果乘到当前是正数，返回max，如果是负数，除以这段路程中，前面的最大负数，再max，如果是0，一切重新初始化 赋值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        max_neg = float('-inf')
        res = float('-inf')
        temp = 1
        for i in range(len(nums)):
            temp*=nums[i]
            if temp>0:
                res = max(res, temp)
            elif temp<0:
                if max_neg!=float('-inf'):
                    res = max(res, temp//max_neg) 
                else:
                    res = max(res, temp)
                max_neg = max(max_neg, temp)
            else:
                temp = 1
                max_neg = float('-inf')
                res = max(res,0)
        return res
        
执行用时：48 ms, 在所有 Python3 提交中击败了83.08%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了44.13%的用户



