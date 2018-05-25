class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        result = -1
        if len(a) < len(b):
            a, b = b, a
        for i in range(len(a)):
            for j in range(1, len(a)+1):
                if a[i:j] not in b and j - i > result:
                    print(a[i:j])
                    result = j - i
        return result
