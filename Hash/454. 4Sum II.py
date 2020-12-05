#一开始想用bfs 不能用的理由： 之前bfs都是把target做root，然后每次创造孩子节点（减去可取的值）
#这里abcd都有两个元素 没有合适的root，除非让0做root
#之前的题目是存在即可，这里还要统计个数，用树的思想+set()保留每层节点 无法剪枝
#其实相当于直接暴力
#哎 我是猪 新方法： 统计a+b的所有结果的频次，判断-c-d是否在counter里
#我以为在的话是+1，其实是+频次，同样的结果的不同次，是不同的组合，都要算一次的
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        abcount = collections.Counter([a+b for a in A for b in B])
        count = 0
        for c in C:
            for d in D:
                count += abcount.get(-c-d, 0)
        return count

执行用时：244 ms, 在所有 Python3 提交中击败了96.03%的用户
内存消耗：38.2 MB, 在所有 Python3 提交中击败了25.56%的用户
