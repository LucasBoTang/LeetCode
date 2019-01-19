class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels_map = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels, positions = [], []

        for i in range(len(s)):
            if s[i] in vowels_map:
                vowels.append(s[i])
                positions.append(i)

        cur = 0
        for pos in positions[::-1]:
            s_list[pos] = s[positions[cur]]
            cur += 1

        return ''.join(s_list)
