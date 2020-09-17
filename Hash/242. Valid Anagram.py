class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter=collections.Counter(s)
        t_counter=collections.Counter(t)
        result=True
        if len(s_counter)!=len(t_counter):
            return False
        for i in range(len(s)):
            if s[i] not in t_counter or s_counter[s[i]]!=t_counter[s[i]]:
                result=False
        return result

'''执行用时：
72 ms, 在所有 Python3 提交中击败了28.68%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了92.66%的用户'''
