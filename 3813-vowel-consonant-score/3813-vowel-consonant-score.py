from math import floor
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        count1 = 0
        count2 = 0

        for ch in s:
            if ch in vowels:
                count1+=1
            elif ch.isalpha():
                count2+=1

        if count2 > 0:
            return count1//count2
        else:
            return 0