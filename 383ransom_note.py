class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for alpha in set(ransomNote):
            if ransomNote.count(alpha) > magazine.count(alpha):
                return False
        return True
