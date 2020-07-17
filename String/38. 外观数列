#如果处理不到最后一个 就先给list加一个空项吧
class Solution:
    def countAndSay(self, n: int) -> str:
        nums = ['1']
        #第n个数只需计算n-1次
        for i in range(n-1):
            count = 1
            num_temp = []
            nums.append('')
            #这样就可以执行到最后一个数字
            for j in range(len(nums)-1):
                if nums[j] == nums[j+1]:
                    count += 1
                else:
                    num_temp.append(str(count))
                    num_temp.append(nums[j])
                    count=1
            nums = num_temp
        return ''.join(nums)

'''执行结果：
通过
执行用时：
32 ms, 在所有 Python3 提交中击败了99.54%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了6.67%的用户'''
