class Solution:
    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start != end and start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True

    def recurse(self, s, j, past, palindromes):
        if j == len(s):
            # print('exit')
            palindromes.append(past)
            return

        valid_palindrome_partitions = []
        # 1, 3
        # 2, 3
        # print(str(past))
        for i in range(j+1, len(s)+1):
            # 0->1 'a'
            # 0->2 aa'
            # 1->2 'a'
            if self.isPalindrome(s[j:i]):
                # [1,2]
                valid_palindrome_partitions.append(i)
        # [1,2]
        # print(valid_palindrome_partitions)
        for i in valid_palindrome_partitions:
            self.recurse(s, i, past + [s[j:i]], palindromes)


    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        self.recurse(s, 0, [], palindromes)
        return palindromes