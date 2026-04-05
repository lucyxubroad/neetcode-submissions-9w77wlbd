class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len = 0, 0
        char_frequency = defaultdict(int)
        for i in range(len(s)):
            char_frequency[s[i]]+=1
            # window_len = i-l+1
            while (i-l+1)-max(char_frequency.values())>k:
                char_frequency[s[l]]-=1
                l+=1
            max_len = max(i-l+1, max_len)
        return max_len
            
            


