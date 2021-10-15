class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]]<temp:
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return res
        
执行用时：192 ms, 在所有 Python3 提交中击败了62.16%的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了26.72%的用户
