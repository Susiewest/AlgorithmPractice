是n>>=1不是n=>>1啦quq
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n&1 == 1:
                count += 1
            n = n>>1
        return count

执行用时：28 ms, 在所有 Python3 提交中击败了99.15%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了15.17%的用户
