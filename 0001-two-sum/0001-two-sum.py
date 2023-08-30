class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverseMap = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in  reverseMap:
                return [reverseMap[remain], idx]
            else:
                reverseMap[num] = idx
        