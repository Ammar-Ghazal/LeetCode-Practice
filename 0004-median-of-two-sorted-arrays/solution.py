class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # size1 = len(nums1)
        # size2 = len(nums2)

        # totalsize = size1 + size2
        # totalnum = 0
        # for i in range(size1):
        #     totalnum += nums1[i]
        # for j in range(size2):
        #     totalnum += nums2[j]
        # return totalnum/totalsize

        total = nums1 + nums2
        totalsize = len(total)
        total.sort()

        if(totalsize%2 == 0):
            second = totalsize/2
            first = second - 1
            return ((total[int(first)]+total[int(second)])/2)
        else:
            first = math.floor(totalsize/2)
            return total[int(first)]
