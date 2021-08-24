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


#从这个方法里学到了 1. 滑动窗口思想 不一定要用一个list保存所有的 每次可以只保留maxlen的 节省了空间复杂度
#2. 最长xxx/子串 就可以用滑动窗口
#3. 不重复 涉及出现次数，需要用hash
#4. 可以理解为双指针做法 需要一个左指针 和一个记录左指针每次应该挪到的下一位
#5. 记得有个题也是比较了下标位置 回头找一下 ✨
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subscript={} #保存如果当前字符重复的话 已有字符串里当前字符最后一次出现的位置
        maxlen=0
        k=0   #记录每次找字符串起始的位置 最开始是0 表示最左端
        for index, character in enumerate(s):
            #！！！！！一开始写的>k 结果不对 debug发现 会忽略掉字母就在起始位置k 下一次要在k+1开始的情况
            if character in subscript.keys() and subscript[character]>=k:
                #上次出现的下标大于当前长度的起始下标
                #起始位置变 最终出现的位置变
                k=subscript[character]+1
                subscript[character]=index
            else:
                subscript[character]=index
                maxlen=max(maxlen,index-k+1)
        return maxlen


0824 我想的是maxlen的更新可以放在if里执行，也就是每遇到重复字母就更新一次，但这样的话，如果完整字符串没有重复字母，那么maxlen将不会更新，如果字符串为' '，期望返回1而不是0
而且如果是aab这种，左指针指向第二个a，右指针指向b也不会更新maxlen 不对不对不对额


