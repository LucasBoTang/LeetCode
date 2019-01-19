class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for letter in s:
            dict[letter] = dict.get(letter, 0) + 1
        evens, odds, have_odds = 0, 0, False
        for count in dict.values():
            if count % 2:
                odds += count - 1
                have_odds = True
            else:
                evens += count
        if have_odds:
            return evens + (odds + 1)
        else:
            return evens
