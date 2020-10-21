class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        merged=[]
        #这个写法要学习
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)):
            if len(merged)==0 or intervals[i][0]>merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][0]=min(merged[-1][0],intervals[i][0])
                merged[-1][1]=max(merged[-1][1],intervals[i][1])
        return merged
        
'''执行用时：
52 ms, 在所有 Python3 提交中击败了64.33%的用户
内存消耗：
14.4 MB, 在所有 Python3 提交中击败了10.17%的用户'''
