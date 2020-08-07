class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0: return True
        #大写全部转小写
        s=s.lower()
        string_s=''
        #s_list=s.split(' ') 不行 句子里还有其他标点符号 split也不支持设置多个分隔符
        #只保留字符串中小写字母
        for i in range(len(s)):
            #if ord(s[i]) <= 122 and ord(s[i]) >= 97:
            #错了 还要保留数字 用.isalnum()判断是否为字母数字混合
            if s[i].isalnum():
                # string_s.join(s[i])
                string_s += s[i]
        # .join() 方法中传递的参数需要是可迭代的，
        # a.join(b) ，比如 b=123456，是可以迭代的。这个方法的作用就是把a插入到b中每个字符中。1a2a3a4a5a6就是输出。
        # ''.join([a, b]) 是比较常见的用法。 '' 是空字符，意味着在a, b之间加入空字符，也就是将a, b进行了连接。
        length=len(string_s)
        for j in range(length//2):
            if string_s[j]!=string_s[length-j-1]:
                return False
        return True


‘’‘执行结果：
通过
执行用时：
64 ms, 在所有 Python3 提交中击败了51.91%的用户
内存消耗：
13.8 MB, 在所有 Python3 提交中击败了71.57%的用户‘’‘
