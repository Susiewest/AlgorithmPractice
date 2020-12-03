#回顾下46题硬copy[:] 题解有self.original = list(self.original)的写法，相当于新建了一个list
也可以写为 array = original.copy() 这样更加清晰。实际上，array = original[:], array[:] = original, array = original.copy(), array=list(original) 都正确。
array[:] = original写法的解释：
  先定义 array (例如，array=[0]*n, array=[None]*n, n 代表 original 的长度），然后再用 array[:] = original，就可以保证 array 和 original 值相同，但不是同一个对象。
以下方法的shuffle是随机取一个下标，将对应的数放在return数组的当前位置

class Solution:

    def __init__(self, nums: List[int]):
        self.temp = nums
        #self.original = self.temp 察觉到这么写不对，这样temp变了，original也会跟着变
        #array=original，这句话把original地址复制给了array，即两个变量指向同一个对象，这样如果之后改变array的值的话，original的值也会改变。
        #上面的写法相当于起了个别名，除非写b = a[:]，或者b = a.copy()
        self.original = nums.copy()


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.temp = self.original.copy()
        return self.temp


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.aux = self.temp.copy()
        for i in range(len(self.temp)):
            remove_idx = random.randrange(len(self.aux)) #这里不能写temp的长度，为了不重复取值，我们的aux每次取了以后会pop掉，所以aux的长度会变化，写temp长度随机取下标会越界
            self.temp[i] = self.aux.pop(remove_idx)
        return self.temp





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
执行用时：272 ms, 在所有 Python3 提交中击败了81.30%的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了71.99%的用户


可以随机取两个牌互换，但是这样呢无法保证照顾到每一张牌，对于n张牌组成的有序排列，经过了n次随机选择，漏掉1只牌从未选过的概率不等于0，而且，随着牌的张数数量增加，这个概率非常可观。
Fisher–Yates算法倒序遍历，每次在当前元素之前的下标中随机选择一个元素互换，然后就固定了当前元素，继续向前
洗n次，会得到n！种结果，此时，已经完全充满n！的空间，洗更多次，样本空间不扩充。
这样做利用了抽卡本身的顺序，【保证照顾】到了每一张原本序列中的卡，

而简单粗暴随机抽取存在出现重复位置的可能性，就等于浪费了一次排序的机会，

换句话说，其等效抽卡次数因为出现了过去相同的洗法，有效洗牌次数下降，样本空间缩小，无法充满整个n！空间，所以有效性会下降。

而Fisher–Yates算法在原理上保证了不会出现浪费次数，重复选择的情况，导致样本空间一直保持n！，没有坍缩，这就是其在数学意义上优秀的原因。

链接：https://leetcode-cn.com/problems/shuffle-an-array/solution/xi-pai-suan-fa-xiang-jie-by-jackwener/

class Solution:

    def __init__(self, nums: List[int]):
        self.temp = nums
        #self.original = self.temp 察觉到这么写不对，这样temp变了，original也会跟着变
        #上面的写法相当于起了个别名，除非写b = a[:]，或者b = a.copy()
        self.original = nums.copy()


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.temp = self.original.copy()
        return self.temp


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.temp)):
            swap_idx = random.randrange(i,len(self.temp)) #当前元素可以取到
            self.temp[i], self.temp[swap_idx] = self.temp[swap_idx], self.temp[i]
        return self.temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

执行用时：268 ms, 在所有 Python3 提交中击败了81.73%的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了78.29%的用户
