class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        tail = len(s) - 1
        head = 0
        s_list = list(s)

        while (head < tail):
            while head < tail and s_list[head] not in vowels:
                head += 1

            while (tail > head and s_list[tail] not in vowels):
                tail -= 1
            
            s_list[head], s_list[tail] = s_list[tail], s_list[head]
            head += 1
            tail -= 1
        return "".join(s_list)