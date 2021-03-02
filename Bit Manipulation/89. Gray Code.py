数学推导法：
设G(n)是n位格雷编码的所有结果，则G（n+1）:
  1. 将G(n)每个编码前面加‘0’得到G'(n)
  2. 将G'(n)反转得到镜像R(n)，在R(n)中的每个元素前添加1得到R'(n)  Attention!!!是把增加一位后的G'(n)的第一个元素+1，也就是G(n)的新一位+1 
  # 为啥要反转，因为格雷编码要求 两个连续的数值仅有一个位数的差异
  3. 将G'(n)与R'(n)合并得到G(n+1)
 
编码思路：
        1. 初始化G(0)和位数标识head
        2. 外层循环次数为总位数n
        3. 内层循环倒序遍历res(对应上述第2步反转),位数标识加上当前索引对应的值即为R'(n)中的元素
        4. 在res后追加上述计算的元素，遍历结束，得到Gray编码集
  
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result, head = [0], 1
        for i in range(n):
            # 两个连续的数值仅有一个位数的差异
            for j in range(len(result)-1, -1, -1):
                result.append(head+result[j])
            head <<= 1
        return result
执行用时：56 ms, 在所有 Python3 提交中击败了49.22%的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了33.40%的用户

