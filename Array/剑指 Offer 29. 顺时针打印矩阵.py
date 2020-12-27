class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        result = []
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            for j in range(top+1, bottom+1):
                result.append(matrix[j][right])
            #如果left==right or top==bottom，就不用执行下面了，会重复
            #所以是两个都不满足的时候才执行，中间用and
            if left<right and top<bottom:          
                for i in range(right-1,left-1,-1):
                    result.append(matrix[bottom][i])
                for j in range(bottom-1,top,-1):
                    result.append(matrix[j][left])
            top+=1
            left+=1
            right-=1
            bottom-=1
        return result
执行用时：32 ms, 在所有 Python3 提交中击败了99.55%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了18.95%的用户

