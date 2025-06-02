#创建一个prefix tree然后实现insert, search 以及startwith三个函数功能
class TrieNode:
    """
    初始化一个constructor用来构建TrieNode, 每一个node有两个属性,children字典和endOfWord来代表它是不是一个单词的结尾
    字典里面的key就是单一的字符串,value是另一个trieNode
    """
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: #如果当前字符串不再字典里
                cur.children[c] = TrieNode() #把字符串的字符作为key然后把TrieNode作为value
            cur = cur.children[c] #把cur指针更新为当前的TrieNode
        cur.endOfWord = True #最后标记当前的children为一个单词的末尾

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        