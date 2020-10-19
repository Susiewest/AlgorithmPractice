class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0: return []
        left, right=0, len(matrix[0])-1
        top, bottom=0, len(matrix)-1
        result=[]
        while(left<=right and top<=bottom):
            for col in range(left,right+1):
                result.append(matrix[top][col])
            #为什么会没写range。。。无语
            for row in range(top+1,bottom+1):
                result.append(matrix[row][right])
            #当left==right或者top==bottom 说明此时只剩最后一行/一列要处理
            #只需从左到右/从上到下遍历一次即可 前两个for可满足要求
            #不必再从右到左 从下到上重复遍历
            if left<right and top<bottom:
                for col in range(right-1,left,-1):
                    result.append(matrix[bottom][col])
                for row in range(bottom,top,-1):
                    result.append(matrix[row][left])
            left, right, top, bottom=left+1, right-1, top+1, bottom-1
        return result
        
'''执行用时：
40 ms, 在所有 Python3 提交中击败了65.24%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了5.43%的用户'''
