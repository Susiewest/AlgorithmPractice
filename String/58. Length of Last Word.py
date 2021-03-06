class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        last=''
        for i in range(1,len(s)+1):
            last=s.split(' ')[-i]
            #是‘’不是‘ ’
            if last!='':
                return len(last)
        return len(last)


'''执行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了43.11%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了5.26%的用户'''
