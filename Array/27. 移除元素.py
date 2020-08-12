class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pointer]=nums[i]
                pointer+=1
        #循环最后一步+1了 返回长度不必再+1
        return pointer
        
 '''执行结果：
通过
执行用时：
36 ms, 在所有 Python3 提交中击败了88.30%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了7.14%的用户'''
