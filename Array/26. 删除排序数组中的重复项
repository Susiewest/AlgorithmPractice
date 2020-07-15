class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]:
                pointer+=1
                nums[pointer]=nums[i+1]
        return pointer+1

'''执行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了88.97%的用户
内存消耗：
14.6 MB, 在所有 Python3 提交中击败了8.16%的用户'''
