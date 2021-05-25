class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(x[::-1] for x in words)
        repeat = 0
        for i in range(1,len(words)):
            if not words[i].startswith(words[i-1]):
                repeat = repeat + 1 + len( words[i-1])
        return repeat + 1 + len(words[-1]) 
        


class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
