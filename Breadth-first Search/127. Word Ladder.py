此题最大收获 代码逻辑没有问题了依然会在wordlist里有很多单词的时候超时，核对了题解发现，答案使用了set（wordlist）替代了wordlist
后面验证新词是否在词典里时，也使用的 if newword not in set： 
即使wordlist看起来没有重复的词，增加这个trick了以后也不再超时了 让我猜测 是否用set在数据结构上会比list更快？

还有个双向bfs写法 不想写了 好累 好难

33/43
#广度优先遍历，因为我们也不用回溯，因为不需要完全建立图，只要走一步看下步就好
#边走边建立联系 如果变换字母后in wordlist-->（1）到了吗？到了返回当前层数+1
#（2）没到 当前词visited 加入bfs的queue
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue=collections.deque()
        length=len(beginWord)
        #wordList.remove(endWord)
        level=1
        visited=set(beginWord)
        queue.append(beginWord)
        while(queue):
            nodes=len(queue)
            for i in range(nodes):
                cur=queue.popleft()
                word_list=list(cur)
                for j in range(length):
                    original_char=word_list[j]
                    for k in range(26):
                        word_list[j]=chr(ord('a')+k)
                        new_word=''.join(word_list)
                        if new_word in wordList:
                            if new_word==endWord:
                                return level+1
                            #else:
                            if new_word not in visited:
                                visited.add(new_word)
                                queue.append(new_word)
                    word_list[j]=original_char #不写这一步 hit变换h直到zit，再变换i，z就一直没变回去！！
            level+=1
        return 0


AC：
#广度优先遍历，因为我们也不用回溯，因为不需要完全建立图，只要走一步看下步就好
#边走边建立联系 如果变换字母后in wordlist-->（1）到了吗？到了返回当前层数+1
#（2）没到 当前词visited 加入bfs的queue
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordset=set(wordList)  #解决超时问题改动1
        queue=collections.deque()
        length=len(beginWord)
        #wordList.remove(endWord)
        level=1
        visited=set(beginWord)
        queue.append(beginWord)
        while(queue):
            nodes=len(queue)
            for i in range(nodes):
                cur=queue.popleft()
                word_list=list(cur)
                for j in range(length):
                    original_char=word_list[j]
                    for k in range(26):
                        word_list[j]=chr(ord('a')+k)
                        new_word=''.join(word_list)
                        if new_word in wordset: #解决超时问题改动2
                            if new_word==endWord:
                                return level+1
                            #else: #解决超时问题改动3
                            if new_word not in visited:
                                visited.add(new_word)
                                queue.append(new_word)
                    word_list[j]=original_char #不写这一步 hit变换h直到zit，再变换i，z就一直没变回去！！
            level+=1 #忘了写 超时
        return 0 #解决return none问题

执行用时：460 ms, 在所有 Python3 提交中击败了35.79%的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了71.84%的用户
