#看解题区才知道原来我写的这就算是动态规划了。。

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        if numRows>=1:
            pascal.append([1])
        for i in range(1,numRows):
            temp=[]
            temp.append(1)
            for j in range(1,i):
                temp.append(pascal[i-1][j-1]+pascal[i-1][j])
            temp.append(1)
            pascal.append(temp)
        return pascal



'''执行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了39.59%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了92.67%的用户'''
