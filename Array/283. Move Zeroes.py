class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #双指针
        pre = 0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pre]=nums[i]
                pre+=1
        for i in range(pre, len(nums)):
            nums[i]=0

执行用时：32 ms, 在所有 Python3 提交中击败了98.52%的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了26.32%的用户
