#乘积=当前数左边的乘积*右边的乘积 左边一遍右边更新一遍
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        for i in range(len(nums)):
            result.append(temp) #记录当前元素左侧数字的乘积
            temp*=nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i]*=temp
            temp*=nums[i]
        return result

执行用时：64 ms, 在所有 Python3 提交中击败了70.92%的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了61.31%的用户
