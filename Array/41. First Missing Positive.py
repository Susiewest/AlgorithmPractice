又是一个鸽巢原理，对负数不做处理，以及对位置正确的数结束while循环。
还有对特殊的测试用例边界的考虑。如果数字都在该在的位置上，返回多少？如果数字放不到位置上，返回多少？
测试用例[7,8,9,10,11，-1，-2]， 不能直接写min（num）>1 就return 1 里面有负数干扰视线

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            #有坑 测试用例[7,8,9,10,11] 如果数字放不到位置上，不限制nums[i]的范围小于len，会导致越界
            while 0<nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i]!=i+1: #如果数字放不到位置上
                return i+1 
        #有坑 测试用例 []/[1]/[1,2]
        return len(nums)+1 #如果数字都在该在的位置上

执行用时：40 ms, 在所有 Python3 提交中击败了63.96%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了10.45%的用户

