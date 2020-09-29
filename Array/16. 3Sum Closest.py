#一开始让approx=0了，比较abs（）的时候会出错，应该取的极端大或者极端小的值
#我这里让前三个之和为初始值了
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return False
        approximate=nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)):
            left, right=i+1, len(nums)-1
            while(left<right):
                threesum=nums[i]+nums[left]+nums[right]
                if abs(threesum-target)<abs(target-approximate):
                    approximate=threesum
                if threesum==target:
                    return target
                elif threesum>target:
                    right-=1
                else:
                    left+=1
        return approximate
        
        
'''执行用时：
140 ms, 在所有 Python3 提交中击败了40.55%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了52.31%的用户'''
