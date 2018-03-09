class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.hash[number] = self.hash.get(number, 0) + 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        while not len(self.hash):
            return False
        for num1 in self.hash.keys():
            num2 = value - num1
            if num1 == num2 and self.hash[num1] > 1:
                return True
            if num1 != num2 and num2 in self.hash:
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
