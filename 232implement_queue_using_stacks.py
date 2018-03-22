class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        temp = []
        for _ in range(len(self.queue)):
            temp.append(self.queue[-1]) # stack top
            self.queue.pop() # stack pop
        self.queue.append(x) # stack top
        for _ in range(len(temp)):
            self.queue.append(temp[-1]) # stack top
            temp.pop() # stack pop


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = self.queue[-1] # stack top
        self.queue.pop() # stack pop
        return temp


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[-1] # stack top


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not len(self.queue)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
