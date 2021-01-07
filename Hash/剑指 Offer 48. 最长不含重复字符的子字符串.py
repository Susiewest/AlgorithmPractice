和第3题一致
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = end = 0
        chart = {}
        while(end<len(s))：
        #只有出现位置处于当前判断子串内部才更新start 
        不然老早就跳过去了 现在更新start又回退了
            if s[end] in chart and chart[s[end]]>=start:
                start=chart[s[end]]+1
            chart[s[end]]=end
            if end-start+1>max_len:
                max_len=end-start+1
            end+=1
        return max_len
        
执行用时：56 ms, 在所有 Python3 提交中击败了97.83%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了18.91%的用户

