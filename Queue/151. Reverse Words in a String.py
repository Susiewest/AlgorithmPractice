冷酷无情的API选手需要注意，s.split()是多个连续空格当作一个划分 s.split(' ')就真是一个空格当做一次划分
ps： s.split()可以去掉开头结尾的，不需要另外s.strip()

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        return ' '.join(temp[::-1])
执行用时：64 ms, 在所有 Python3 提交中击败了6.00%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.84%的用户

双端队列法
word保存当前单词，完整后保存到双端队列，从左端送入
双端队列的appendleft优于list的insert
有两个地方需要注意 1. word被加入result的判断条件，如果只在遇到空格时就加入，遇到连续的两个空格会保留一个空格，这样是不对的。因此在遇到空格并且word不为空时加入。
2. 最后一个单词遇不到空格 无法正确加入result，因为结束前要再加入一次
ps：仍然不是O(1)空间
class Solution:
    def reverseWords(self, s: str) -> str:
        start, end = 0, len(s)-1
        while s[start]==' ':
            start+=1
        while s[end]==' ':
            end-=1
        result = collections.deque()
        word = []
        while(start<=end):
            if s[start]!=' ':
                word.append(s[start])
            # "a good   example"-->"example good a"
            elif s[start]==' ' and word:         #1
                result.appendleft(''.join(word))
                word = []
            start+=1
        result.appendleft(''.join(word))      #2
        return ' '.join(result)
   
执行用时：56 ms, 在所有 Python3 提交中击败了13.48%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.35%的用户

