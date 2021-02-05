找第k大 也就是排序后找第len-k位置的数
不想全排序 可以用快排 只处理小于pivot的数放在前面，检测下标是不是len-k
不是的话再分治，此时只需分治一侧 称之为通过pivot减而治之
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #用partition之前切记加一步随机，防止性能退到O(N^2)
        #不加随机，当测试用例是近乎有序的情况，递归树会退化成链表，时间复杂度从O(NlogN)编程O(N^2)
        def partition(nums, left, right):
            random_num = random.randint(left, right) #随机选择一个位于l r之间的数和left交换
            nums[random_num], nums[left] = nums[left], nums[random_num]
            pivot = nums[left]
            index = left
            for i in range(left+1, right+1):
                if nums[i]<pivot:
                    index+=1
                    nums[i], nums[index] = nums[index], nums[i] #把小于pivot的都换到前面去 大于的可以不管
            nums[left], nums[index] = nums[index], nums[left]#index之前的顺序不重要，重要的是left的真正位置要换过去
            return index
        
        target = len(nums)-k 
        left, right = 0, len(nums)-1
        index = -1
        while(index!=target):
            index = partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index>target:
                right = index-1
            else:
                left = index+1

执行用时：44 ms, 在所有 Python3 提交中击败了84.08%的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了81.85%的用户

#这个把快排写完整的方法会超时捏。。
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,left, right):
            #本来想传参只传局部的nums[left,right]，不用指定left，right
            #但是想到这样怎么才能知道现在固定的元素下标是len-k呀
            random_num = randint(left, right)
            nums[left], nums[random_num] = nums[random_num], nums[left]
            pivot = nums[left]
            pivot_index = left
            left+=1
            while left<right:
                while left<right and nums[left]<=pivot: left+=1
                nums[right], nums[left] = nums[left],nums[right]
                while left<right and nums[right]>pivot: right-=1
                nums[right], nums[left] = nums[left],nums[right]
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            return left
        index = -1
        left, right = 0, len(nums)-1
        target = len(nums)-k
        while index!=target:
            index = partition(nums,left,right)
            if index==target:
                return nums[index]
            elif index>target:
                right = index-1
            else:
                left = index+1
        
改了快排partition对换部分可以了
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,left, right):
            #本来想传参只传局部的nums[left,right]，不用指定left，right
            #但是想到这样怎么才能知道现在固定的元素下标是len-k呀
            random_num = random.randint(left, right)
            nums[left], nums[random_num] = nums[random_num], nums[left]
            pivot = nums[left]
            index = left
            for i in range(left+1,right+1):
                if nums[i]<pivot:
                    index+=1
                    nums[index], nums[i] = nums[i], nums[index]
            nums[left], nums[index] = nums[index], nums[left]
            return index
        index = -1
        left, right = 0, len(nums)-1
        target = len(nums)-k
        while index!=target:
            index = partition(nums,left,right)
            if index==target:
                return nums[index]
            elif index>target:
                right = index-1
            else:
                left = index+1
执行用时：48 ms, 在所有 Python3 提交中击败了65.61%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了34.65%的用户
我的疑惑：1. while的写法和if的写法都要遍历整个num，为什么while会超时 if不会，难道说交换步骤很费时间？
2. 找到left==right停止循环，此时把pivot和停止位置元素对换，如何保证停止的位置小于pivot呢？
解答：原来确实是上面写的快排有些问题，按下面写可以通过
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,left, right):
            #本来想传参只传局部的nums[left,right]，不用指定left，right
            #但是想到这样怎么才能知道现在固定的元素下标是len-k呀
            random_num = randint(left, right)
            nums[left], nums[random_num] = nums[random_num], nums[left]
            pivot = nums[left]
            pivot_index = left
            while left<right:
                while left<right and nums[right]>pivot: right-=1
                nums[left] = nums[right]
                while left<right and nums[left]<=pivot: left+=1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
        index = -1
        left, right = 0, len(nums)-1
        target = len(nums)-k
        while index!=target:
            index = partition(nums,left,right)
            if index==target:
                return nums[index]
            elif index>target:
                right = index-1
            else:
                left = index+1
执行用时：36 ms, 在所有 Python3 提交中击败了96.13%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了42.12%的用户

快排的一点总结：partition的写法，要么for循环遍历一遍，一个指针保留替换位置，一个指针工作，遇到小的就送到替换位置去（和替换位置互换）
要么就两个while，从right--开始，因为left指着的地方要被比pivot小的顶掉，才能保证left位置元素的正确性，不然按我上面那么疯狂互换，额 好像也可以，关键在于不能像我那样从left/left+1做起。。。
写for的时候要互换，因为要把前面不小于pivot的换到后面来，写while的时候可以互换，也可以不互换，单方面覆盖left/right位置，效果差不多。关键是要从right--开始。
