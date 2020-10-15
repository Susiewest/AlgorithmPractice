import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=collections.defaultdict(list)
        #这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
        #这里呢就是建立了一个dict，当key值不存在时，默认value是个空list吧。。
        for s in strs:
            count=[0 for _ in range(26)]
            for i in s:
                count[ord(i)-ord('a')]+=1
            result[tuple(count)].append(s)
        return list(result.values())
        
        
'''执行用时：
76 ms, 在所有 Python3 提交中击败了30.64%的用户
内存消耗：
18.2 MB, 在所有 Python3 提交中击败了6.69%的用户'''

#哎我的问题可太多了 太菜了 别人几行代码解决的问题 我还对别人代码很多基础疑问。。。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for s in strs:
            #1. 还学到一点，如果不想改变原本的字符串s，可以不要写s.sort()而是sorted(s)
            #会另外创建个新的返回
            #2. s.sort()会报错 说str没有sort() 那么为啥sorted就行呢。。。
            #3. +s 不行 不能把list和str concate，所以要写+[s]
            #4. 为什么加了tuple就可以做键值
            #result[tuple(s.sort())]=result.get(tuple(s.sort()),[])+[s]
            result[tuple(sorted(s))]=result.get(tuple(sorted(s)),[])+[s]
        return list(result.values())
'''执行用时：
56 ms, 在所有 Python3 提交中击败了89.37%的用户
内存消耗：
16.4 MB, 在所有 Python3 提交中击败了43.68%的用户'''
