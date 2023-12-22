class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        num_ones = sum(data)
        # init
        max_ones = num_ones_sub = sum(data[:num_ones])
        # slide window
        for i in range(num_ones, len(data)):
            num_ones_sub = num_ones_sub + data[i] - data[i-num_ones]
            # find max num of 1
            max_ones = max(max_ones, num_ones_sub)
        return num_ones - max_ones
