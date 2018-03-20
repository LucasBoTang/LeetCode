class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.insert(0, x) # queue push
        for _ in range(len(self.queue) - 1):
            temp = self.queue[-1] # queue peek
            self.queue.insert(0, temp) # queue push
            self.queue.pop() # queue pop


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        temp = self.queue[-1] # queue peek
        self.queue.pop() # queue pop
        return temp


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[-1] # queue peek


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.queue)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
