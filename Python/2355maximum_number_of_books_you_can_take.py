class Solution(object):
    def maximumBooks(self, books):
        """
        :type books: List[int]
        :rtype: int
        """
        dp_table = [0] * len(books)
        for i in range(len(books)):
            dp_table[i] = self.takeLastBooks(books[:i+1])
        return max(dp_table)            

    def takeLastBooks(self, books):
        """
        :type books: List[int]
        :rtype: int
        """
        num_books = 0
        # take all books from last shelf
        cur_shelf = books.pop()
        num_books += cur_shelf
        # continue to take books from previous shelf
        while books and cur_shelf > 1:
            cur_shelf = min(cur_shelf - 1, books.pop())
            num_books += cur_shelf
        return num_books
