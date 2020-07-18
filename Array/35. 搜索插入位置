class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]<target:
                i+=1
            else:
                return i
                
  '''执行结果：
通过
执行用时：
32 ms, 在所有 Python3 提交中击败了97.54%的用户
内存消耗：
14.4 MB, 在所有 Python3 提交中击败了7.14%的用户'''
