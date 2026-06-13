class Solution:
    def decode(self, index, s, seen):
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index in seen:
            return seen[index]
        ways = self.decode(index+1, s, seen)
        if int(s[index:index+2])<= 26 and index+1 < len(s):
            ways += self.decode(index+2, s, seen)
        seen[index] = ways
        return ways


    def numDecodings(self, s: str) -> int:
        return self.decode(0,s, {})
        