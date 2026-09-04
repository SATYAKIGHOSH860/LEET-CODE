class Solution:
    def secondHighest(self, s: str) -> int:
        number = []
        for i in s:
            if i.isdigit():
                number.append(i)
        number = set(number)
        if len(number) <2:
            return -1

        number = [int(x) for x in number]
        number.sort()
        return number[-2]