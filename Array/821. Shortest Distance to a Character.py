方法一：保存c出现的位置，再对每个元素计算所有差值绝对值取最小
方法二：正向走一遍+反向走一遍 正向记录走过的最近的，反向记录走过的最近的

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # index_chart = {}
        c_list = []
        result = []
        for i in range(len(s)):
            if s[i]==c:
                c_list.append(i)
        for i in range(len(s)):
            temp = float('inf')
            for index in c_list:
                temp = min(temp,abs(i-index))
            result.append(temp)
        return result

执行用时：136 ms, 在所有 Python3 提交中击败了5.42%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了54.20%的用户

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_list = []
        result = []
        prev = float('-inf')
        for i in range(len(s)):
            if s[i]==c:
                prev = i
            #这里不是else才append，而是每个位置都要append，只好让前面无c的位置为正无穷
            result.append(i-prev)
        # 这里不再是-inf了，不然减去-inf就是正数+inf=null了
        prev = float('inf')
        for j in range(len(s)-1, -1, -1):
            if s[j]==c:
                prev = j
            else:
                result[j] = min(result[j],prev-j)            
        return result
            
执行用时：36 ms, 在所有 Python3 提交中击败了98.95%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.94%的用户


