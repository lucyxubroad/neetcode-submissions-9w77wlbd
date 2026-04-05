class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = {}
        for c in t:
            target[c] = 1 + target.get(c, 0)
        
        observed = {}
        start, end = 0, 0

        min_substring = ""
        exists = False

        while end < len(s):
            if s[end] in target:
                observed[s[end]] = 1 + observed.get(s[end],0)
            # print(start,end, s[start:end+1], target, '|', observed)
            while all(observed.get(key,0) >= target[key] for key in target.keys()):
                while start < end and s[start] not in target:
                    start += 1
                if exists is False:
                    min_substring = s[start:end+1]
                else:
                    min_substring = s[start:end+1] if end-start+1 < len(min_substring) else min_substring
                exists = True
                if s[start] in observed:
                    observed[s[start]] -= 1
                start += 1
            end += 1

        return min_substring


