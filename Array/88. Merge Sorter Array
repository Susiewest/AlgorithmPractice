class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point=m+n-1
        i=m-1
        j=n-1
        while(i>=0 and j>=0):
            if nums1[i]>nums2[j]:
                nums1[point]=nums1[i]
                i-=1
            else:
                nums1[point]=nums2[j]
                j-=1
            point-=1
        if i<0:
            nums1[:j+1]=nums2[:j+1]
        return nums1
           
 '''Runtime: 40 ms, faster than 59.76% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 42.81% of Python3 online submissions for Merge Sorted Array.'''
