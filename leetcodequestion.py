# First Letter to Appear Twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = []
        for i in s:
            if a.count(i) == 1:
                return i
            else:
                a.append(i)
        return ""
