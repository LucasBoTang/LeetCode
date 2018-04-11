class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        n, m = len(word), len(abbr)
        while j < m:
            cur = 0
            while abbr[j].isdigit():
                cur = cur * 10 + int(abbr[j])
                if not cur:
                    return False
                if j + 1 < m:
                    j += 1
                else:
                    return i + cur == n
            i += cur
            if i >= n or word[i] != abbr[j]:
                return False
            i += 1
            j += 1
        return True
