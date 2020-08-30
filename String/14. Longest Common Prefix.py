class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #zip函数 把多个list对应位置的元素打包成元组：[fff][lll][ooi]
        #groups=zip(strs)
        #列表、元组前面加星号作用是将列表解开成两个独立的参数，传入函数，字典前面加两个星号，是将字典解开成独立的元素作为形参。
        groups=zip(*strs)
        count=''
        #for i in range(len(groups)):
        for i in groups:
            if len(set(i))==1:
                #count+=str(set(i)) 输出"{'f'}{'l'}" 而预期是‘fl’
                count+=i[0]
            else:
                return count
        return count
     
''' 执行结果：通过
执行用时：
52 ms, 在所有 Python3 提交中击败了20.47%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了6.15%的用户'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #垂直扫描法
        if len(strs)==0:
            return ''
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                #or前后的句子不能写反 不然会strs[j][i]的i越界
                if i==len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return strs[j][:i]
        #return '' 怎么脑子里想的返回空啊 循环执行完了可能是第一个list太短了 应该返回strs[0]
        return strs[0]

'''执行结果：通过
执行用时：
44 ms, 在所有 Python3 提交中击败了60.96%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了6.15%的用户'''

#看到有个人找出list字母序最大的和最小的找公共子序列...这个想法我暂时想不到...
