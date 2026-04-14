class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True  # end of word marker

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            ch = word[i]
            if ch == '.':
                return any(dfs(i + 1, nxt) for k, nxt in node.items() if k != '#')
            return ch in node and dfs(i + 1, node[ch])

        return dfs(0, self.trie)