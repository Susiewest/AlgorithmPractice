完全自己想的思路&写的题解 find mid-reverse-concate
为什么题解里合并没有考虑l1/l2多一个的情况 哦！知道了 合并部分写的不完全一样
答案直接在l1的基础上见缝插针 我是另外起了一个result，合并二者，所以我最后没有那步 l2.next=l1 还要另外处理
他的答案是 l1.next=l2 l1=l1temp l2.next=l1 l2=l2temp 这样处理到最后 l2.next=l1 解决了奇数个节点时，前半个链表比后半个链表长1的情况
还有个答案是list存节点再按下标访问

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        #find mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second
        p = slow.next #the first node
        #一开始没这句话 报错说listnode里发现了cycle
        slow.next = None
        r = p.next
        dummy = ListNode(-1)
        dummy.next = None
        while p:
            #把这行放在这里可以避免写在while最后 p=r=none r=p.next none无next的问题，也就是确认p不为空了再取他的next
            r = p.next
            p.next = dummy.next
            dummy.next = p
            p = r
        result = ListNode(-1)
        #concate head and dummy
        p1 = head
        p2 = dummy.next
        cur = result
        while p1 and p2:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
            cur.next = p2
            p2 = p2.next
            cur = cur.next
        cur.next = p1 or p2
        return result.next

执行用时：108 ms, 在所有 Python3 提交中击败了45.44%的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了48.66%的用户

