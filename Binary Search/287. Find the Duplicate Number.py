#惹 一开始用异或 结果想起来异或是很多对重复的找不重复的
#用sum(num)减去1+2+...+n结果才发现测试用例不一定是每个数都出现的
#之前那个每个数都会出现的题目是268题 题干说 Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array. 
#此题为Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. [1,4,4,2,4] [2,2,2,2,2]等都有可能

这个二分法和以前的二分法不一样，以前的二分是二分数组下标，这个二分是缩小搜索的值域范围

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1 #取值范围的左右边界[1, n]
        while(left<right):
            count = 0
            mid = left + (right - left)//2
            for i in range(len(nums)):
                if nums[i]<=mid:
                    count+=1
            if count>mid:
                right = mid
            #震惊 把if >改成else就不超时了。。
            else:
                left = mid+1
        return left
        
执行用时：72 ms, 在所有 Python3 提交中击败了43.28%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了45.39%的用户
