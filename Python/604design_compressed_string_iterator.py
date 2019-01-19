class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """

        self.letter = []
        self.count = []
        self.len = 0
        self.index = (0, 0)

        i = 0
        count = 0
        while i < len(compressedString):
            char = compressedString[i]
            if char.isalpha():
                self.count.append(count)
                self.len += 1
                self.letter.append(char)
                count = 0
            elif char.isdigit():
                count = count * 10 + int(char)
            i += 1
        self.count = self.count[1:]
        self.count.append(count)


    def next(self):
        """
        :rtype: str
        """

        if self.hasNext():
            i, j = self.index
            next_letter = self.letter[i]

            j += 1
            if j < self.count[i]:
                self.index = (i, j)
            else:
                self.index = (i+1, 0)

        else:
            next_letter = ' '

        return next_letter


    def hasNext(self):
        """
        :rtype: bool
        """
        i, j = self.index
        return i < self.len



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressself.lenedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
