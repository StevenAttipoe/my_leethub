class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        word_dic = defaultdict(list)


        for word in words:
            word_dic[word[0]].append(word)

        for char in s:
            words = word_dic[char]
            word_dic[char] = []

            for word in words:
                if len(word) == 1:
                    count += 1
                else:
                    word_dic[word[1]].append(word[1:])

        return count