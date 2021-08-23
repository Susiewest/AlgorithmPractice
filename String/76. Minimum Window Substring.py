滑动窗口，s里包含t的最短覆盖串

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = collections.defaultdict(int)
        for c in t:
            count[c] += 1
        needcount = len(t)
        left = 0
        result = (0, float(inf))
        for i in range(len(s)):
            if count[s[i]]>0:
                needcount -= 1
            count[s[i]] -= 1
            if needcount==0:
                while True:
                    if count[s[left]]==0:
                        break
                    count[s[left]] += 1
                    left += 1
                if i-left<result[1]-result[0]:
                    result = (left,i)
                count[s[left]] += 1
                needcount += 1
                left += 1
        return '' if result[1]>len(s) else s[result[0]:result[1]+1] 
            

执行用时：88 ms, 在所有 Python3 提交中击败了64.34%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了14.70%的用户
