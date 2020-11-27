用双指针法和查表法重写一遍
双指针：先排序再双指针，小的多走，等于就加入result，大的就不走
查表法：一个数组用counter来计数，另一个数组每个数字在counter里对应的key值-1（if value>0)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=set(nums1)&set(nums2)
        result = []
        for i in intersection:
            result+=[i]*min(nums1.count(i),nums2.count(i))
        return result
        
执行用时：104 ms, 在所有 Python3 提交中击败了8.67%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.54%的用户
