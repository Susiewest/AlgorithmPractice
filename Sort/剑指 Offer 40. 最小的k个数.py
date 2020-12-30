写堆排序的时候，干啥都别忘heapq诶
求最小的k要维护大根堆
heap默认小根堆，做大根记得元素都取负数
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0: return []
        hp = [-arr[i] for i in range(k)]
        heapq.heapify(hp)
        for i in range(k,len(arr)):
            if -arr[i]>hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp,-arr[i])
        result = [-item for item in hp]
        return result
执行用时：64 ms, 在所有 Python3 提交中击败了67.95%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了7.86%的用户

