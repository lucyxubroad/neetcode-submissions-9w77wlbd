'''
When we encounter a ., we need to do a BFS. 
    Add all the possible options to the search. Pass in next char to search for.

When inserting, we can insert as a trie. 
    Every node points to the next char (stored in a dictionary)
    Example:
        insert tree + tries

        t --> r --> e --> e
                --> i --> e --> s

        start_node = node
        for (index, char) in enumerate(word):
            # this will either return a node that already exists 
            # or it creates the next node and returns it
            is_last_char = index == len(word) - 1
            start_node = next_char_node(start_node, char, is_last_char) 

            # note: the match is only true if the last char of 
            # what you are searching for is also the last char
            # of the word in the trie. so we DO need to indicate 
            # if char is the last char

        when you do a search, you can do a BFS

        char_index = 0 (next letter we are searching for)

        while char_index < len(word):
            to_search = [node]
            char_we_are_searching_for = word[char_index]
            if word[char_index] == '.':
                # add everything to to_search
            else:
                find the next char from current node
                if not found, then return FALSE
        
        add to list with (index, char looking for)

        while to search is not empty:
            at this current node, add all the possible next nodes to the list --> in the same tuple
            if you encounter a node that is the last char and it matches, then you return true

        return node.is_last is true 

'''
class Node:
    def __init__(self, char):
        self.char = char
        self.next_chars = {}
        self.is_last_char = False
    
    def nextChar(self, char, is_last_char):
        if char in self.next_chars:
            char_node = self.next_chars[char]
            char_node.is_last_char = is_last_char or char_node.is_last_char
            return char_node
        else:
            char_node = Node(char)
            char_node.is_last_char = is_last_char
            self.next_chars[char] = char_node
            return char_node
        
class WordDictionary:

    def __init__(self):
        self.start_node = Node('')

    def addWord(self, word: str) -> None:
        char_node = self.start_node
        for (index, char) in enumerate(word):
            char_node = char_node.nextChar(char, index == len(word)-1)

    def search(self, word: str) -> bool:
        to_search = [(self.start_node, 0)]
        while len(to_search) > 0:
            (search_node, search_index) = to_search.pop(0)
            if search_index > len(word)-1:
                print(search_node.char)
                return search_node.is_last_char
            search_char = word[search_index]
            if search_char == '.':
                search_chars = search_node.next_chars.values()
                for ch in search_chars:
                    to_search.append((ch, search_index+1))
            else:
                if search_char in search_node.next_chars:
                    to_search.append((search_node.next_chars[search_char], search_index+1))
        
        return False


        
