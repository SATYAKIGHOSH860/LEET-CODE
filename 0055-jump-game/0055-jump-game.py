class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            new_reach = i + nums[i]
            if new_reach > farthest:
                farthest = new_reach

        return True