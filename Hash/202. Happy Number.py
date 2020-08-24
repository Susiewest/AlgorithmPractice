#这个题题解区有一个很屌的快慢指针做法 做法不难 难的是想到这个办法 过一段时间再回来做这个题试试
#目前的办法是用了一个hashset判断有无重复出现的数
#要么n=1结束循环 要么出现重复的数结束循环 最后return n等不等于1 等于就是true 不等于就是不快乐的数
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            new_num=0
            while(n):
                last=n%10
                new_num+=last**2
                n=n//10
            return new_num
        num_sets=set()
        while n!=1 and n not in num_sets:
            num_sets.add(n)
            n=next_num(n)
        return n==1



'''执行用时：
48 ms, 在所有 Python3 提交中击败了56.11%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了91.67%的用户'''
