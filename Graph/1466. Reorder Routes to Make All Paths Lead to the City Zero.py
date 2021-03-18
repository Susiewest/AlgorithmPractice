class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections = sorted(connections, key = lambda x:x[1])
        result = 0
        accessible_city = {0}
        #对于排序不是由小到大的 可能到最后一个元素accessible才增加了新元素
        #这个时候不能结束 还要继续从头往后加入，直到accessible city满n个
        while len(accessible_city)<n:
            for left,right in connections:
                # 如果right已经是0
                if right in accessible_city:
                    accessible_city.add(left)
                elif left in accessible_city:
                    result += 1
                    accessible_city.add(right)
        return result
执行用时：120 ms, 在所有 Python3 提交中击败了74.51%的用户
内存消耗：29.4 MB, 在所有 Python3 提交中击败了66.67%的用户

