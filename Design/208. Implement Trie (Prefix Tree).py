字典树，感觉就是字典套字典，每个节点为字典的键值 也就是一个字母，字典的value又是一个字典，键值保存当前字母的下一个字母们
存完一个完整单词 记得设置end符号 通常用‘#’ 
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = '#'
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        if '#' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


执行用时：120 ms, 在所有 Python3 提交中击败了99.28%的用户
内存消耗：26.2 MB, 在所有 Python3 提交中击败了50.97%的用户
