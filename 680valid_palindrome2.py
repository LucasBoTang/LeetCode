class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i, j = 0, len(s) - 1
        delete = 0

        while i <= len(s) // 2:
            if s[i] == s[j]:
                i += 1
                j -= 1

            else:
                if delete:
                    return False
                delete += 1

                temp1 = s[i+1:j+1]
                temp2 = s[i:j]
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]

        return True
