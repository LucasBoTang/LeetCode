class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slist = [word.lower() for word in s if word.isalnum()]
        return slist == slist[::-1]
