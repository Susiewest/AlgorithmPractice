连续顺子五张牌的隐形条件：最大值-最小值<5，且每张牌仅出现一次
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        poker_set = set()
        max_poker, min_poker = 0, 14
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            if nums[i] in poker_set:
                return False
            max_poker = max(max_poker, nums[i])
            min_poker = min(min_poker, nums[i])
            poker_set.add(nums[i])
        return max_poker-min_poker<5
执行用时：32 ms, 在所有 Python3 提交中击败了94.26%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了14.89%的用户


        
