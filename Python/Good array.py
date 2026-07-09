class Solution:
    def isGood(self, nums):
        nums.sort()
        n = len(nums) - 1

        for i in range(n):
            if nums[i] != i + 1:
                return False

        return nums[n] == n
