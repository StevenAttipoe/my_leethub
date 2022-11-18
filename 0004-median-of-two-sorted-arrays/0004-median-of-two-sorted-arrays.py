class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)):
            temp = nums1
            nums1 = nums2
            nums2 = temp
            
        l, r = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        
        while True:
            partX = (l + r) // 2
            partY =  half - partX - 2
            
            leftX = nums1[partX] if partX >= 0 else float("-inf")
            rightX = nums1[partX + 1] if (partX+1) < len(nums1) else float("inf")
            
            leftY = nums2[partY] if partY >= 0 else float("-inf")
            rightY = nums2[partY + 1] if (partY+1) < len(nums2) else float("inf")
            
            if leftX <= rightY and leftY <= rightX:
                if total % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY) ) / 2.0
                
                else:
                    return min(rightX, rightY)
                
            if leftX > rightY:
                r = partX - 1
            else:
                l = partX + 1
        return -1