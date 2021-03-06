动态规划，设置三个指针指向第一个丑数，每个丑数都是之前的某个丑数*2或者3或者5
三个指针同时遍历，分别掌管当前数*2/3/5
在各种可能的拼接相乘里选择最小的一个，选完了这个数*2/3/5就不能再选了，于是指向下一个数

一个丑数乘以 2， 3， 5 之后， 一定还是一个丑数。
并且如果从丑数序列首个元素开始 *2 *3 *5 来计算， 丑数序列也是不会产生漏解的。
合并 3 个有序序列， 最简单的方法就是每一个序列都各自维护一个指针， 然后比较指针指向的元素的值， 将最小的放入最终的合并数组中， 并将相应指针向后移动一个元素。
存在重复的解的， 例如 nums2[2] == 3*2, nums3[1] == 2*3 都计算出了 6 这个结果， 所以在合并 3 个有序数组的过程中， 还需要跳过相同的结果，
这也就是为什么在比较的时候， 需要使用 3 个并列的 if... if... if... 而不是 if... else if... else 这种结构的原因。 
当比较到元素 6 时， if (dp[i] == dp[p2] * 2)...if (dp[i] == dp[p3] * 3)... 可以同时指向 nums2, nums3 中 元素 6 的下一个元素。


作者：mrsate
链接：https://leetcode-cn.com/problems/chou-shu-lcof/solution/chou-shu-ii-qing-xi-de-tui-dao-si-lu-by-mrsate/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。丑数序列实际上就是这 3 个有序序列对的合并结果， 计算丑数序列也就是相当于 合并 3 个有序序列。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        a, b, c = 0, 0, 0
        for i in range(1,n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i]==n2: a+=1
            if dp[i]==n3: b+=1
            if dp[i]==n5: c+=1
        return dp[-1]
    
执行用时：128 ms, 在所有 Python3 提交中击败了93.72%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了19.08%的用户
