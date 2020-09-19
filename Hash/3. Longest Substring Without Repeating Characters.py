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
