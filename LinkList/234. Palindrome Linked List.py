# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        copylist=[]
        while(head):
            copylist.append(head.val)
            head=head.next
        return copylist==copylist[::-1]
   
'''执行用时：
108 ms, 在所有 Python3 提交中击败了12.83%的用户
内存消耗：
23.2 MB, 在所有 Python3 提交中击败了51.00%的用户'''
#啊真是弱鸡的做法呢。。。但是最后那个原本是想写个for循环从两端开始判断 后来发现可以酱紫写 感觉很牛批 但还是 额效果好差
#b = a[i:j:s]表示：s表示步进，缺省为1. 所以a[i:j:1]相当于a[i:j]
#当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
