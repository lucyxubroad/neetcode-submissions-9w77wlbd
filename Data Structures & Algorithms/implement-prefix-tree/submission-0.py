class PrefixNode:
    def __init__(self, value, isEnd):
        self.value = value
        self.children = {} # value -> PrefixNode
        self.isEnd = isEnd
    
    def __str__(self):
        return 'value: ' + self.value  + 'isEnd: ' + str(self.isEnd)

    def insertChild(self, character, isEnd):
        if character in self.children:
            charNode = self.children[character]
            if isEnd:
                charNode.isEnd = True
            return charNode
        else:
            charNode = PrefixNode(character, isEnd)
            self.children[character] = charNode
            return charNode

class PrefixTree:

    def __init__(self):
        self.firstNode = PrefixNode('_', False)
        self.prefixNodes = {
            '_': PrefixNode('_', False)
        } 

    def insert(self, word: str) -> None:
        word = '_' + word
        c = 0
        nodes = self.prefixNodes
        while c < len(word) and word[c] in nodes:
            node = nodes[word[c]]
            nodes = node.children
            if c == len(word) - 1:
                node.isEnd = True
            c += 1
        while c < len(word):
            node = node.insertChild(word[c], (c==len(word)-1))
            c += 1

    def search(self, word: str) -> bool:
        word = '_' + word
        nodes = self.prefixNodes[word[0]].children
        c = 1
        while c < len(word) and word[c] in nodes:
            node = nodes[word[c]]
            nodes = node.children
            c += 1
        # print (word,(c == len(word)),node.isEnd  )
        return (c == len(word)) and (node.isEnd)

    def startsWith(self, prefix: str) -> bool:
        word = '_' + prefix
        nodes = self.prefixNodes[word[0]].children
        c = 1
        while c < len(word) and word[c] in nodes:
            node = nodes[word[c]]
            nodes = node.children
            c += 1
       
        return (c == len(word))
        
        