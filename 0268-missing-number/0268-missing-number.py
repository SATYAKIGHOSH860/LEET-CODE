class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = []
        n = len(nums)
        nums = sum(nums)
        result = sum(range(n+1))
        return result - nums