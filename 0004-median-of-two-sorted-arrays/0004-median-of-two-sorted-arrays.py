class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        lenNums = len(nums)
        nums = sorted(nums)

        if lenNums % 2 == 1:
            return nums[lenNums // 2]
        else:
            return (nums[lenNums // 2] + nums[lenNums // 2 - 1]) / 2
