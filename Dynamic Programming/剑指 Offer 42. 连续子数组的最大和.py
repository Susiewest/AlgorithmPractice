class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #nums中全是负数的时候要return最大值，靠后面判断大于0无法实现
        if max(nums)<0:
            return max(nums)
        scan = []
        temp = 0
        for i in range(len(nums)):
            if temp+nums[i]>0:
                temp += nums[i]
                scan.append(temp)
            else:
                scan.append(0)
                temp = 0
        return max(scan)
执行用时：72 ms, 在所有 Python3 提交中击败了72.57%的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了5.07%的用户
