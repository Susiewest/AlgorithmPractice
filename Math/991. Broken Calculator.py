class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # 逆向思维 Y只能除以2或者+1
        # 乘除肯定比加减快
        result = 0
        while Y>X:
            result += 1
            if Y%2: Y += 1
            else: Y = Y//2
        return result+X-Y #最后的差距只能一个一个来

执行用时：36 ms, 在所有 Python3 提交中击败了76.76%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了50.00%的用户

