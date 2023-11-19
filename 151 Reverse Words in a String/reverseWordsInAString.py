class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        rev_list = s_list[::-1]
        return(' '.join(rev_list))