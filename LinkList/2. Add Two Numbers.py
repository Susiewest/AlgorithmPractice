# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#这个解题的思路是 用temp来记录进位用于下一轮循环
#每对结点相加的时候立刻创建对应结果结点 处理进位
#一开始超时了 那是因为忘了大家一起next 还是要在脑子里有个动画
#后来报错说none没有next属性 所以给l1=l1.next搞了个条件
#说了这么多其实还是。。题解区nb
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode(None)
        pointer=result
        temp=0
        while l1 or l2 or temp:
            temp=(l1.val if l1 else 0) + (l2.val if l2 else 0)+temp
            pointer.next=ListNode(temp%10)
            temp=temp//10
            pointer=pointer.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return result.next


'''执行用时：
76 ms, 在所有 Python3 提交中击败了62.12%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了76.55%的用户'''
