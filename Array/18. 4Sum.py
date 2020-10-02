class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        length=len(nums)
        if length<4 or nums[0]+nums[1]+nums[2]+nums[3]>target: 
            return []
        for i in range(0,length-2):
            if i>1 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,length-1):
                left, right=j+1,length-1
                #一开始忘了写while 只返回了一个结果。。。
                #双指针勿忘while 无语子
                while(left<right):
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        #本来是没有写这个的 但是while避免了left和right的重复，却避免不了j的重复
                        #把j的重复单独写出来结束循环 又会遗漏解 没有办法只能写出这么不优美的代码了。。。
                        if [nums[i],nums[j],nums[left],nums[right]] not in result:
                            result.append([nums[i],nums[j],nums[left],nums[right]])
                        #忘了保证内部的left<right的绝对性
                        while(left<right and nums[right-1]==nums[right]):
                            right-=1
                        while(left<right and nums[left+1]==nums[left]):
                            left+=1
                        right-=1
                        left+=1
                    elif temp>target:
                        right-=1
                    else:
                        left+=1
        return result
        

'''执行用时：
836 ms, 在所有 Python3 提交中击败了61.55%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了68.46%的用户'''
