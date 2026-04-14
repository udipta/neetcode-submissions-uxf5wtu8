class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word at terminal node

    def addWord(self, w):
        for ch in w:
            self = self.children.setdefault(ch, TrieNode())
        self.word = w

class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] == '#' or
                board[r][c] not in node.children
            ):
                return

            ch = board[r][c]
            nxt = node.children[ch]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited
            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)
            board[r][c] = ch

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)

        return res