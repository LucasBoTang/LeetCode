class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash = {}
        for word in s:
            hash[word] = hash.get(word, 0) + 1
        odd = 0
        for count in hash.values():
            if count % 2:
                odd += 1
        return odd == 0 or odd == 1
