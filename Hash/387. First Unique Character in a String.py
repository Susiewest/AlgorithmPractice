用.count 结合for循环可能有O(n2)的时间复杂度
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #还有“cc”这种return -1
        # if not s:
        #     return -1
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1

执行用时：5756 ms, 在所有 Python3 提交中击败了8.04%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了7.79%的用户

这个先hash再遍历 应该是O(2n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1

执行用时：96 ms, 在所有 Python3 提交中击败了87.33%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了8.38%的用户
