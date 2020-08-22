class Solution:
    def hammingWeight(self, n: int) -> int:
        last, count=0, 0
        while(n):
            last=n&1
            if last==1:
                count+=1
            n=n>>1
        return count



'''执行用时：
48 ms, 在所有 Python3 提交中击败了26.55%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了13.36%的用户'''
