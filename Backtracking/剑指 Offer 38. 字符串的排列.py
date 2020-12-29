题解用后面每个字母和当前位置互换，我感觉有点绕弯
下面这个做法，每次把除了当前位置之外的字符串传进去，感觉非常清晰
class Solution:
    def permutation(self, s: str) -> List[str]:
        result = []
        def backtrack(s, path):
            if not s:
                result.append(path)
            #visited的作用是当前位置的某个字母只允许出现一次，避免因有两个相同字母带来的重复结果
            visited = set()
            for i in range(len(s)):
                if s[i] not in visited:
                    backtrack(s[:i]+s[i+1:],path+s[i])
                    visited.add(s[i])
        backtrack(s,'')
        return result
执行用时：152 ms, 在所有 Python3 提交中击败了60.29%的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了27.02%的用户
