练习桶排序&堆排序

方法一： hash+排序 暴力 时间复杂度O(nlogn) 空间复杂度O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        有一个问题，counter对象在sort完会变成list，有点奇怪 [1,1,1,2,3] counter:{1:3,2:1,3:1} sort:[[1,3],[2,1],[3,1]]
        freq_sort = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(freq_sort[i][0])
        return result
        #return freq_sort[:k][0] 这么写不对哦，返回的是切片后的第一个元素，即[1, 3]
 
执行用时：40 ms, 在所有 Python3 提交中击败了98.24%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了25.41%的用户

counter的函数most_common 学习
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return [i[0] for i in freq.most_common(k)]

 
 方法二：hash+桶排序/拉链法 空间换时间 时间复杂度优化到O(n)
 
 
 方法三：HeapSort 
 topk （前k大）用小根堆，维护堆大小不超过 k 即可。每次压入堆前和堆顶元素比较，如果比堆顶元素还小，直接扔掉，否则压入堆。检查堆大小是否超过 k，如果超过，弹出堆顶。复杂度是 nlogk
 求前 k 大，用小根堆，求前 k 小，用大根堆。
 使用大根堆，当海量数据时，存储将是瓶颈。使用小根堆的话，只需存储k个元素。
 
 heappush(heap, x) 将x压入堆中
 heappop(heap)    从堆中弹出最小的元素 使用heap[0] ，可以只访问最小的元素而不弹出它。
 
1. 所以heapq模块只能搞小根堆，return最小值，想要找topk，就得所有频次取反找最小k
2. 压入堆时，以（负的频次，元素值）的形式，这样才能找到前k个频次对应的元素，此外，找最小的k个负频次，如果写成（item，-freq[item]) heappop就只能返回item的最小k
3. import xxx的写法，下面就必须要加xxx.function
如果是from xxx import * 的写法，下面就不用加

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap, result = [], []
        for item in freq:
            heapq.heappush(heap, (-freq[item],item))
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

执行用时：40 ms, 在所有 Python3 提交中击败了98.24%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了23.33%的用户
