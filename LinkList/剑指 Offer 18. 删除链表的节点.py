啊这 首先我不用设置两个指针，设置一个指针判断下一个是不是val就可以了。。。。。。。
其次，书上的题目是给出head，给出要删除的节点指针，O(1)复杂度删掉这个节点，方法是把下一个的value复制到当前节点，然后删掉下一个。
我淦，怎么会这么机智，让我想到了之前一个题，O(1)时间复杂度删除数组元素，结合了hash，但是hash只能O(1)时间锁定删除元素的下标，用remove的话还是会达到O(n)的时间复杂度。
解决方法是，把最后一个元素复制到要删除的位置，然后pop最后一个元素。
这招移花接木 小朋友们学废了嘛
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val==val:
            return head.next
        pre, cur = head, head.next
        while cur.val!=val:
            pre = pre.next
            cur = cur.next
        pre.next=pre.next.next
        return head 
执行用时：36 ms, 在所有 Python3 提交中击败了97.80%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.29%的用户

