#算不上回溯 但题解里有其他回溯写法 后面二刷可以写一下
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]       

        result = []
        for i in range(1,len(s)+1):
            left=s[:i]
            right=s[i:]
            if left==left[::-1]:
                right=self.partition(right) #右侧所有的分割结果return
                for j in range(len(right)):
                    #result保存当前字符串s，所有不同的左分割情况，每个左分割内部不同情况append进同一个list，不同左分割在不同的list里，最后一起return回去
                    result.append([left]+right[j])
        return result

执行用时：76 ms, 在所有 Python3 提交中击败了55.54%的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了8.01%的用户
