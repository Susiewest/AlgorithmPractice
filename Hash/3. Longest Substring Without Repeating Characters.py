#写错了 遇到重复字母就从当前字母开始 这个思路不对
#反例 "dvdf"会输出2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding=[]
        temp=''
        for i in range(len(s)):
            if s[i] in temp:
                temp=s[i]
            else: temp+=s[i]
            sliding.append(temp)
        max_len=0
        for i in range(len(s)):
            if len(sliding[i])>max_len:
                max_len=len(sliding[i])
        return max_len


#改成了已存在 就一位一位往右挪 直到不存在 而不是直接挪到当前位置
#遇到一个很麻烦的问题就是temp=‘’ 字符串没法移除最左边的字母 于是我改写成list 然后每次保存进sliding的时候把temp里的拼起来
#性能好差。。明天再看看题解吧
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding=[]
        temp=[]
        for i in range(len(s)):
            if s[i] in temp:
                while(s[i] in temp):
                    del temp[0]
            #else: temp.append(s[i]) 一开始这么写 现在改成下面的写法 因为把已存在的s[i]去掉了
            temp.append(s[i])
            sliding.append(''.join(temp))
        max_len=0
        for i in range(len(s)):
            if len(sliding[i])>max_len:
                max_len=len(sliding[i])
        return max_len
'''执行用时：
140 ms, 在所有 Python3 提交中击败了21.16%的用户
内存消耗：
17.8 MB, 在所有 Python3 提交中击败了5.11%的用户'''
