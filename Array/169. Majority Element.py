class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==element:
                count+=1
            else:
                count-=1
                if count==0:
                    element=nums[i+1]
                    count=0
        count_2=0
        for i in range(len(nums)):
            if nums[i]==element:
                count_2+=1
        if count_2>=len(nums)//2:
            return element
        else:
            return False



'''执行用时：
64 ms, 在所有 Python3 提交中击败了29.61%的用户
内存消耗：
15 MB, 在所有 Python3 提交中击败了88.58%的用户'''
