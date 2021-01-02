class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        comb=[]
        result=[]
        for i in range(len(digits)):
            comb.append(str(digits[i]))
        add_one= int(''.join(comb))+1
        for i in range(len(str(add_one))):
            result.append(int(str(add_one)[i]))
        return result
        
   '''执行结果：
通过
执行用时：
36 ms, 在所有 Python3 提交中击败了88.29%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了6.82%的用户'''
