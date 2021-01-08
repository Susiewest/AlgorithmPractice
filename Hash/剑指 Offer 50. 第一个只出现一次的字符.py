class Solution:
    def firstUniqChar(self, s: str) -> str:
        chart = collections.Counter(s)
        for i in chart.keys():
            if chart[i]==1:
                return i
        return ' '
执行用时：64 ms, 在所有 Python3 提交中击败了99.00%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了25.53%的用户

