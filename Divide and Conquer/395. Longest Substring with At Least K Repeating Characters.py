对字符串中每个字母统计频次，如果小于k，就以这个字母split分治，如果都大于等于k，那就return length
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        for c in set(s):
            if s.count(c)<k:
                return max(self.longestSubstring(slic,k) for slic in s.split(c)) 
        return len(s)

执行用时：36 ms, 在所有 Python3 提交中击败了92.41%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了21.87%的用户
