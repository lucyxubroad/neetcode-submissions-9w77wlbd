class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts = collections.Counter(s1)
        # print(char_counts)
        for i in range(0, len(s2)-len(s1)+1):
            char_counts_copy = char_counts.copy()
            for j in range(i, i+len(s1)):
                print(j, s2[j])
                if s2[j] not in char_counts_copy:
                    break
                else:
                    char_counts_copy[s2[j]]-=1
                    if char_counts_copy[s2[j]] == 0:
                        char_counts_copy.pop(s2[j])
            # print(char_counts_copy)
            # print()
            if all(value == 0 for value in char_counts_copy.values()):
                return True
        return False