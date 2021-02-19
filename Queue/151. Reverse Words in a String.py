冷酷无情的API选手需要注意，s.split()是多个连续空格当作一个划分 s.split(' ')就真是一个空格当做一次划分
ps： s.split()可以去掉开头结尾的，不需要另外s.strip()

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        return ' '.join(temp[::-1])
执行用时：64 ms, 在所有 Python3 提交中击败了6.00%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.84%的用户

双端队列法待补充
