#对一个数 令字典里 他和target的差值对应的value是自己的index
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)==0:
            return False
        hashdic={}
        for index, num in enumerate(numbers):
            #这样写不行 先存自己再判断 只会把自己也算做备选里
            #比如输入【2，3，4】 会选33 而不是42 这个程序只有走到4才知道有2可以选
            #而现在走到3就停了 会选【3，3】
            #hashdic[target-num]=index
            #if num in hashdic.keys():
                #return hashdic[num]+1,index+1
            if num in hashdic.keys():
                return hashdic[num]+1,index+1
            hashdic[target-num]=index
        return False


'''执行结果：
通过
执行用时：
40 ms, 在所有 Python3 提交中击败了90.62%的用户
内存消耗：
14.1 MB, 在所有 Python3 提交中击败了68.00%的用户'''

        
