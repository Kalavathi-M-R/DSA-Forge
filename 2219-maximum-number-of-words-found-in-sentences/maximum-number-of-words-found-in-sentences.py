class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count = []
        for sentence in sentences:
            count.append(sentence.count(" ")+1)
        return max(count)