# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        temp = [''] * 4    # default characters because we do not have real file
        while True:
            count = min(read4(temp), n - index)
            for i in range(count):
                buf[index] = temp[i]
                index += 1
            if index == n or count < 4:
                return index
