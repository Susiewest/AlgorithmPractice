class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transform={'None':' '}
        if len(s)!=len(t): return False
        for i in range(len(s)):
            #'ab'和'aa'输出true 实际是false
            if s[i] not in transform.keys() and t[i] not in transform.values():
                transform[s[i]]=t[i]
        s_trans=''
        for i in range(len(s)):
            try:
                s_trans+=transform[s[i]]
            except:
                s_trans+=transform['None']
        if s_trans==t:
            return True
        return False

'''执行用时：
60 ms, 在所有 Python3 提交中击败了32.34%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了70.03%的用户'''
