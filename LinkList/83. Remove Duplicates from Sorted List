class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        pre = head
        current = head.next
        while current:
            if current.val == pre.val:
                 pre.next=current.next
                 current=current.next
                #current=current.next
                #这样写不行 [1,1,2,3,3] 经过我的处理会变成[1,2,3,3] 最后一个3没被覆盖掉
            else:
                pre.next = current
                current = current.next
                pre=pre.next
        return head
'''Success
Details 
Runtime: 40 ms, faster than 87.64% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.6 MB, less than 97.37% of Python3 online submissions for Remove Duplicates from Sorted List.'''
