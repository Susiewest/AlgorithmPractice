liweiwei答案评论有学习动归的建议
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/

如果题目只问最优解，没有问具体解，一般使用动态规划完成，而不应该使用回溯算法
动态规划三要素：dp[i]的定义 转移方程 初始化 
dp[i]代表的是，以nums[i]为结尾的，之前任意可能的位置为起点到此的最大上升子序列长度。而非到nums[i]为止的最大升序子数组长度。 
也就是说，用这个[10, 9, 2, 5, 3, 7, 1, 18]序列跑 ，1的那个位置跑出来是1 ，不是3 
从这个题我学习到，动态规划可以写一种数组最后一个位置即题解的转移方程，也可以写一个答案蕴藏在dp数组中，可以最后取一个最大值/最小值的转移方程
换句话说，可以让dp[i]保存到当前位置的最优解（nums[i]参与/不参与来对比），也可以保存nums[i]为结尾参与的最优解

转移方程 遍历到nums[i]时，需要把之前的数字全都看一遍，只要nums[i]严格大于某个数，nums[i]就可以跟在这个数的后面，形成一个更长的升序子序列 
dp[i]=下标i之前小于nums[i]的对应的状态值（dp值）的最大值+1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
        
执行用时：3752 ms, 在所有 Python3 提交中击败了5.03%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.36%的用户

那么将dp（为了区分 这里叫tail） 将tail[j]定义为保存到nums[i]为止的最大升序子数组的末尾数，j是最大升序子数组的长度，最后tail的长度就是想要的解
也就是，遇到一个nums[i]，和tail[-1]比较，如果大，就跟在后面，如果小，就去更新整个tail里第一个比nums[i]大的数，为了保存同样长度，末尾数最小的子数组！

以下的写法是错误的！测试用例为[4,10,4,3,8,9] 的时候，遇到第二个4，会去tail=[4,10]里先找到4，发现4不满足大于nums[i]会去右边找到10，然后替换掉10，这样不对
所以27行说的找到第一个大于nums[i]不对，应该找到第一个大于等于nums[i]的，那么等号的处理方式应该和大于绑定，不应该和小于绑定，如果和小于绑定了，left会去找小于等于nums[i]的下一个！

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>tail[-1]:
                tail.append(nums[i])
                continue
            if nums[i]==tail[-1]:
                continue
            left, right = 0, len(tail)-1
            while(left<right):
                #mid = left+(right-left)//2
                mid = (left+right)>>1
                if tail[mid]>nums[i]:
                    #right = mid-1
                    right = mid
                else:
                    left = mid+1
            tail[left] = nums[i] #left最后会指向第一个大于nums[i]的
        return len(tail)

以下为正确写法

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>tail[-1]:
                tail.append(nums[i])
                continue
            if nums[i]==tail[-1]:
                continue
            left, right = 0, len(tail)-1
            while(left<right):
                #mid = left+(right-left)//2
                mid = (left+right)>>1
                if tail[mid]<nums[i]:
                    #right = mid-1
                    left = mid+1
                else:
                    right = mid
            tail[left] = nums[i] #left最后会指向第一个大于nums[i]的
        return len(tail)
    
执行用时：72 ms, 在所有 Python3 提交中击败了75.22%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了26.91%的用户
