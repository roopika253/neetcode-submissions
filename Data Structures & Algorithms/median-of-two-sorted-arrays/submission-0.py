class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        arr = [0]*(m+n)
        i = 0
        j = 0
        k = 0
       
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                arr[k] = nums1[i]
                k += 1
                arr[k] = nums2[j]
                k += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                k += 1
                i += 1
            else :
                arr[k] = nums2[j]
                k += 1
                j += 1
        while i < m:
            arr[k] = nums1[i]
            k += 1
            i += 1
        while j < n:
            arr[k] = nums2[j]
            j += 1
            k += 1
       
        length = m+n
        indx = length // 2
      
        if length % 2 == 0:
           
            return (arr[indx-1] + arr[indx])/2
        else :
            return (arr[indx])
        