弱鸡暴力做法。。。
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        result = []
        for i in range(len(nums)-k+1):
            result.append(max(nums[i:i+k]))
        return result

执行用时：476 ms, 在所有 Python3 提交中击败了35.62%的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了8.82%的用户

