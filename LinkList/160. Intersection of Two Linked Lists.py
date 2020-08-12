#哎写的方法好笨啊 先遍历两个链表获得长度差 再让长的先走长度差个再长短一起走 直到指的节点一致
#看题解有个很浪漫同时也很牛批的写法 走过对方走过的路 总有一天会相遇 
#两个指针同时遍历 一个走到头了就换到另一链表的头部继续走 走完Y的三个枝桠的长度 就会相遇 有空了闭卷默写下
#下面是本人的笨蛋做法 哼

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return None
        def getLength(node):
            length=1
            while(node.next):
                length+=1
                node=node.next
            return length
        length_a=getLength(headA)
        length_b=getLength(headB)
        dis=abs(length_a-length_b)
        if length_a>length_b:
            for i in range(dis):
                headA=headA.next
        else:
            for i in range(dis):
                headB=headB.next
        while(headA!=headB):
            headA=headA.next
            headB=headB.next
        return headA



'''执行结果：
通过
执行用时：
192 ms, 在所有 Python3 提交中击败了53.61%的用户
内存消耗：
29.1 MB, 在所有 Python3 提交中击败了29.33%的用户'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return None
        Bearbear=headA
        Zhizhi=headB
        while(Bearbear!=Zhizhi):
            if Bearbear!=None:
                Bearbear=Bearbear.next
            else:
                Bearbear=headB
            if Zhizhi!=None:
                Zhizhi=Zhizhi.next
            else:
                Zhizhi=headA
        return Bearbear
        #一开始写的 没有交点的情况下死循环了 是这么写的 
        #bearbear=bearbear.next zhizhi=zhizhi.next
        #if bearbear=none bearbear=headb
        #if zhizhi=none bearbear=heada
        #这样写就把两个同时为none（也就是走过了对方的路依然没有相遇）的情况直接当场解决了 
        #不会留到while判断的时候知道它走完了 直接开始再不断的走
        #现在的写法 不相交时 走完对方的路会同时为空 可以结束循环
        #总结：要判断当前点是不是空 不是就取下一个（如果大家下一个都是空 while就结束了）
        #而不是判断下一个点为不为空 为空立刻回开头这样不对
        #做人要有空窗期 不要无缝衔接 有空窗期才能好好反思是不是没有缘分（我在说什么


'''执行用时：
184 ms
, 在所有 Python3 提交中击败了76.97%的用户
内存消耗：
29 MB, 在所有 Python3 提交中击败了52.29%的用户'''
