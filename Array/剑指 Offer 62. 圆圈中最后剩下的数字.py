昨晚脑子不清楚，觉得每次删除，大家下标就变短一个，而且数组总长度也变短一个。
感觉每次重新算下一个下标的时候很混乱，不知道该怎么取正确位置的下标了
今天重新思考（kan ti jie)发现，其实每次都是比上次删除的位置+m-1的下标，这个-1就可以正确取到下标了
之前错误的想法是第一次删除，下次取-1，第二次删除 下次要-2了，再加上取余的长度也要变化，这样很乱
其实这次取了-1算出来的当前删除位置start，就是已经调整了所有元素下标了，下次只要调整下次的就好，不用考虑之前的
也就是说，每次找下一个位置的元素还是有迹可循的，有规律的，不是每次都会变化操作的。。。

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        candidate = [i for i in range(n)]
        start = 0
        while n>1:
            start = (start+m-1)%n
            n -= 1
            del candidate[start]
        return candidate[0]
执行用时：2000 ms, 在所有 Python3 提交中击败了33.40%的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了21.84%的用户

https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
    根据最后的元素倒推它在初始数组中的位置
    元素在上一轮的实际位置是+m再取余上一轮的数组元素个数
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        start = 0
        for i in range(2,n+1):
            start = (start+m)%i
        return start
执行用时：88 ms, 在所有 Python3 提交中击败了71.46%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了64.78%的用户


