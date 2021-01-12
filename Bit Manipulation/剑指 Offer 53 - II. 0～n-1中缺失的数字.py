class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result^=i
            result^=nums[i]
        return result
执行用时：56 ms, 在所有 Python3 提交中击败了14.11%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了12.40%的用户
