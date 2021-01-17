统计二进制的每个位置上，这些数里有几个1，不是3的倍数的，表示这一列可以区分那个落单数字。
落单数字的其他位都是0，所以其他位置的1都是3的倍数。
还原数字，把取余后的数一位位加入二进制中。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0]*32
        for i in nums:
            for j in range(32):
                temp = i&1
                count[j]+=temp
                i>>=1
        result = 0
        for i in range(32):
            result <<= 1
            result |= (count[31-i]%3)
        return result
执行用时：476 ms, 在所有 Python3 提交中击败了15.25%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了16.09%的用户

