摩尔投票法 因为题目限制了一定存在众数的情况，所以没有另外判断得到的num是否频次大于1/2
如果不一定存在，还需增加一次循环遍历
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = nums[0],1
        for i in range(1,len(nums)):
            if count==0:
                num=nums[i]
            #学习了这种写法
            count+=1 if nums[i]==num else -1
        return num
执行用时：56 ms, 在所有 Python3 提交中击败了45.25%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了15.48%的用户

            
