class Solution(object):
    def singleNumber(self, nums):
        xor_nums = 0
        for i in nums:
            xor_nums ^= i
        return xor_nums


'''执行结果：
通过
执行用时：
52 ms, 在所有 Python3 提交中击败了40.62%的用户
内存消耗：
15.3 MB, 在所有 Python3 提交中击败了62.77%的用户'''
