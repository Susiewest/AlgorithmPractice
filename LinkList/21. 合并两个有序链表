# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #递归方法
        #终止条件
        if l1==None:
        #不能写l1.val 因为报错none没有val属性
            return l2
        elif l2==None:
            return l1
        if l1.val<l2.val:
            #类里面的一个函数 你要指向自身，就要说明是当前对象的这个函数 所以是self.
            #单独定义一个函数就不用self了
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
            
            
    '''执行结果：通过
执行用时：
48 ms, 在所有 Python3 提交中击败了60.61%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了7.14%的用户'''
