# 208的变种题目,判断一个word是否在prefix tree里面,word存在'.'代表可以是任意的字符串
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        """这里每一个'.'都表示我们需要搜索当前root的全部child,因此这个过程就是深度优先然后回溯的过程-->dfs解法需要再这里被使用.然后dfs里面我们需要考虑应该放
        什么argument,1)index 代表我们当前遍历到word里面的什么位置了 2)root 代表当前遍历的子节点是什么. 这里的dfs没有stop的条件因为我们的for循环自然就有一个范围限定"""
        def dfs(i,root):
            cur = root
            for j in range(i,len(word)):
                c = word[j]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(j+1,child):
                            return True
                        # else:
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0,self.root)