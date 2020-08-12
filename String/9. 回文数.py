class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=str(x)
        for i in range(len(y)//2):
            if y[i]!=y[len(y)-i-1]:
                return False
        return True
        
/*执行结果：
通过

执行用时：
76 ms, 在所有 Python3 提交中击败了89.30%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了5.88%的用户*/
