class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) >= self.size:
            self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
