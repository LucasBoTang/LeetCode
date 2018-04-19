class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result, count = [chars[0]], 1
        for i in range(1, len(chars)):
            if chars[i] == result[-1]:
                count += 1
            else:
                if count > 1:
                    result += list(str(count))
                result += chars[i]
                count = 1
        if count > 1:
            result += list(str(count))
        chars[:] = result
