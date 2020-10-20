#刚好昨晚(2020/10/19)在b站up主的动态里看到了一个面试题 和这个题类似
#区别在于 1. b站那个题 每个位置的数就是固定的可以走的步数，而非此题 是可以走的最大步数。 2. b站题第一步，步长最大为len//2，是可以随便走的，第二步开始就要严格按照每个数组元素值走了，
#那个题用的是从后往前动态规划，维护一个步数数组 再从0到len//2遍历动态规划数组 保存最小的可到达终点的步数
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance=0
        for i in range(len(nums)):
            #这个条件一开始没写
            #要保证 每个遍历到的位置 是在当前最远距离内的 才可以更新max 
            if i<=max_distance:
                max_distance=max(i+nums[i],max_distance)
                if max_distance>=len(nums)-1:
                    return True
        return False
        
'''执行用时：
52 ms, 在所有 Python3 提交中击败了67.68%的用户
内存消耗：
14.6 MB, 在所有 Python3 提交中击败了87.12%的用户'''
