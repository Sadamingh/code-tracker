class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k = 0
                while nums[i+k] == val:
                    k += 1
                    if i + k > len(nums) - 1:
                        return count
                nums[i] = nums[i+k]
                nums[i+k] = val
            count += 1
        return count