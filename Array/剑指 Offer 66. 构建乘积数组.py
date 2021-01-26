class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        result = [0]*len(a)
        temp = 1
        for i in range(len(a)):
            result[i] = temp
            temp *= a[i]
        temp = 1
        for i in range(len(a)-1,-1,-1):
            result[i] *= temp
            temp *= a[i]
        return result
执行用时：56 ms, 在所有 Python3 提交中击败了98.62%的用户
内存消耗：22.6 MB, 在所有 Python3 提交中击败了47.36%的用户

