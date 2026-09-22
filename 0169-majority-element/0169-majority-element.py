class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        count = 0
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        highest_freq = max(freq.values())
        for i in freq:
            if freq[i] == highest_freq:
                return i

        
        
