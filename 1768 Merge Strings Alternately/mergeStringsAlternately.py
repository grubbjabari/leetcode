class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_word = ""
        w1_count, w2_count = 0, 0

        if (len(word2) < 1):
            return word1
        while w1_count < len(word1) and w2_count < len(word2):
            merge_word += word1[w1_count]
            merge_word += word2[w2_count]
            w1_count += 1
            w2_count += 1

        if (len(word1) != len(word2)):
            merge_word += word1[w1_count:]
            merge_word += word2[w2_count:]
        return merge_word