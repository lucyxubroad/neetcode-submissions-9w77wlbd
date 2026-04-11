class Solution:
    def recurse(self, letters, word, digit_index, combos, digits):
        if digit_index == len(digits):
            if word != '':
                combos.append(word)
            return
        
        digit = digits[digit_index]
        for i in letters[digit]:
            self.recurse(letters, word+i, digit_index+1, combos, digits)
        

    def letterCombinations(self, digits: str) -> List[str]:
        
        letter_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        combos = []
        
        self.recurse(letter_map, '', 0, combos, digits)

        return combos