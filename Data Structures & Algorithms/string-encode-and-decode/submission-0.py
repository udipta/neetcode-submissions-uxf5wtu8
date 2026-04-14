class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. Find the delimiter
            j = s.find('#', i)
            # 2. Get the length (the number before #)
            length = int(s[i:j])
            # 3. Slice exactly that many characters after #
            res.append(s[j + 1 : j + 1 + length])
            # 4. Jump to the next length prefix
            i = j + 1 + length
        return res