class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        pascal=[]
        if rowIndex>=1:
            pascal.append([1])
        for i in range(1,rowIndex+1):
            temp=[]
            temp.append(1)
            for j in range(1,i):
                temp.append(pascal[i-1][j-1]+pascal[i-1][j])
            temp.append(1)
            pascal.append(temp)
        return pascal[-1]



‘’‘执行结果：
通过
执行用时：
40 ms, 在所有 Python3 提交中击败了72.19%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了59.34%的用户‘’‘
