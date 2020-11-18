#hard题我唯唯诺诺，easy题我重拳出击
#一开始写s=s[::-1]没能真的改 据说是因为题目让原地改，这个赋值把原来的引用弄丢了
#可以用双指针 一个指0，一个指len-1，while i<j 换，++，--
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length//2):
            s[i], s[length-i-1] = s[length-i-1], s[i]
        return s

执行用时：40 ms, 在所有 Python3 提交中击败了95.89%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了10.38%的用户
