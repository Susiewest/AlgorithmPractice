class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        if len(nums)<3 or nums[0]>0:
            return result
        for i in range(len(nums)):
            if nums[i]>0:
                return result
            left, right= i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while(left<right):
                if nums[i]+nums[left]+nums[right]==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while(left<right and nums[left+1]==nums[left]):
                        left=left+1
                    while(left<right and nums[right-1]==nums[right]):
                        right=right-1
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else: 
                    left+=1
        return result
            

'''执行用时：
1100 ms, 在所有 Python3 提交中击败了36.36%的用户
内存消耗：
15.9 MB, 在所有 Python3 提交中击败了47.71%的用户'''
