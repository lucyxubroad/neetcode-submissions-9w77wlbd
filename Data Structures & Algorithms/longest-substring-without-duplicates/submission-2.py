class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_letters = {}
        start, end, length = 0, 0, (0, "")
        while end <= len(s)-1 and start <= end:
            if s[end] not in seen_letters:
                seen_letters[s[end]] = end
                length = max(length, (end-start+1, s[start:end+1]))
                print(s[end],start,end,length, seen_letters)
                end += 1
            else:
                print('not_equal', s[end],start,end,length, seen_letters)
                new_start = seen_letters[s[end]]+1
                for i in range(start, new_start):
                    seen_letters.pop(s[i]) 
                start = new_start
                # seen_letters.pop(s[end])
           
        (max_length, max_string) = length
           
        return max_length

