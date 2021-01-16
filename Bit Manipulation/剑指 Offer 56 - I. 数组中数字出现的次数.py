判断唯一一个不出现两次的数，异或即可
如果这样的数存在两个，如何找出来
首先想到这样的情况下，假设这两个数是a和b，那么这组数异或得到的结果其实就是a&b，在a&b的结果里，找为1的一位
为什么不找0，因为这位为0意味着a和b在这位上的数一样，没法区分a和b。
通过为1的这位，a和b在这位上不同，可以区分a和b，将a b放在不同的组中，这样再异或即可得到a和b。
那么其他出现两次的数，分别和为1的这位相与，在这位为0/1也分开放，能保证两个相同数一定会被分到同一个组中。也能保证a和b分开。

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in nums:
            temp ^= i
        div = 1
        while div&temp==0:
            div<<=1
        a, b = 0, 0
        for i in nums:
            #如何判断第i位上是不是1，不是相与后判断是不是1，而是相与后不为0即该位为1
            #不是判断i&div是不是1，而是判断不为0即可
            if i&div:
                a^=i
            else:
                b^=i
        return [a,b]
执行用时：56 ms, 在所有 Python3 提交中击败了69.49%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了15.54%的用户

