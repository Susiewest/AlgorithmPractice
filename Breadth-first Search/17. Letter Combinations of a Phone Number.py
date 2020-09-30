class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination=[]
        if not digits:
            return combination
        combination=['']
        tmp=''
        chart=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in digits:
            for _ in range(len(combination)): #对每个新i 当前comb里面的所有都是上层的节点
                tmp=combination.pop(0)
                for j in chart[ord(i)-50]: #ascii码-48转为数字，再-2转为从0开始
                    combination.append(tmp+j)
        return combination
        
        
        
'''执行用时：
36 ms, 在所有 Python3 提交中击败了88.41%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了58.79%的用户'''
