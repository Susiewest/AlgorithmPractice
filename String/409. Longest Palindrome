class Solution:
    def longestPalindrome(self, s: str) -> int:
        #count要大写首字母
        #如果某个字母出现偶数次 那么都能拿来做回文串
        #如果奇数次 那么只有次数i-1个可以组成对子
        #多的那个可作为中心的那个数
        #但是中心数只有一个 所以要加个布尔变量 判断 如果有字母个数为奇数个 那最后可以加上个1
        freq = collections.Counter(s)
        length = 0
        single=False
        for i in freq.values():
            if i%2==1:
                length+=i-1
                single = True
            else:
                length+=i
        if single:
            length+=1
        return length
            


'''执行用时：
44 ms, 在所有 Python3 提交中击败了62.46%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了88.80%的用户'''
