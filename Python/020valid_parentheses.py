class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        lens = len(s)

        while lens != 0 and lens % 2 == 0:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

            if len(s) < lens:
                lens = len(s)
            else:
                lens = 0
                
        return s == ""
