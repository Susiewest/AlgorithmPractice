空间复杂度o(logn) 不符合o（1）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while(fast and fast.next):
            slow = slow.next
            fast =fast.next.next
        #断为两段
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        #合并
        h = new_start = ListNode(-1)
        while left and right:
            if left.val<right.val: 
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return new_start.next

执行用时：360 ms, 在所有 Python3 提交中击败了16.13%的用户
内存消耗：28.8 MB, 在所有 Python3 提交中击败了9.19%的用户

O（1）的写法 以下会超时
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        #h是总的工作指针 dummy是固定的伪头 h1和h2是两段的工作指针
        h, length = head, 0
        #统计长度
        while(h): 
            h=h.next
            length+=1
        dummy = ListNode(-1)
        dummy.next = head
        #interval 1->2->4->8...
        interval = 1
        while(interval<length):
            pre, h = dummy, dummy.next
            #设置h1 h2指定两段的头 统计第二段的长度 因为第二段允许比interval短/也可能后面还有好几段 
            while h:
                h1, count = h, interval
                while h and count:
                    h = h.next
                    count-= 1
                if not h: break #终止条件这里也可能满足 也就是h2这段没有了
                #不写上面这句 下面h2为none可能没有val
                h2, count = h, interval #指向h1+interval-1
                while h and count:
                    h = h.next
                    count-= 1
                length1, length2 = interval, interval-count
                while length1 and length2:
                    if h1.val<h2.val:
                        pre.next = h1
                        h1 = h1.next
                        length1-=1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        length2-=1
                    pre = pre.next
                #pre.next = h1 or h2#这样写应该不行 h1h2都不是空 只是长度走完了
                pre.next = h1 if length1 else h2
                while length1 or length2: 
                    pre=pre.next
                    length1-= 1
                    length2-= 1
                pre.next = h #如果不写这个 下一轮可能走不到赋值就break了
            interval*= 2
        return dummy.next

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        #h是总的工作指针 dummy是固定的伪头 h1和h2是两段的工作指针
        h, length = head, 0
        #统计长度
        while(h): 
            h=h.next
            length+=1
        dummy = ListNode(-1)
        dummy.next = head
        #interval 1->2->4->8...
        interval = 1
        while(interval<length):
            pre, h = dummy, dummy.next
            #设置h1 h2指定两段的头 统计第二段的长度 因为第二段允许比interval短/也可能后面还有好几段 
            while h:
                h1, count = h, interval
                while h and count:
                    h = h.next
                    count-= 1
                if not h: break #终止条件这里也可能满足 也就是h2这段没有了
                #不写上面这句 下面h2为none可能没有val
                h2, count = h, interval #指向h1+interval-1
                while h and count:
                    h = h.next
                    count-= 1
                length1, length2 = interval, interval-count
                while length1 and length2:
                    if h1.val<h2.val:
                        pre.next = h1
                        h1 = h1.next
                        length1-=1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        length2-=1
                    pre = pre.next
                #pre.next = h1 or h2#这样写应该不行 h1h2都不是空 只是长度走完了
                pre.next = h1 if length1 else h2
                while length1>0 or length2>0:    #****************************改了这里就不超时了？？？？？？？？？？？？？？？？？？？？***************************
                    pre=pre.next
                    length1-= 1
                    length2-= 1
                pre.next = h #如果不写这个 下一轮可能走不到赋值就break了
            interval*= 2
        return dummy.next

执行用时：428 ms, 在所有 Python3 提交中击败了8.27%的用户
内存消耗：28.6 MB, 在所有 Python3 提交中击败了15.14%的用户

            
