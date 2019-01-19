class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_index = float('inf')
        common_list = [rest for rest in list1 if rest in list2]
        for rest in common_list:
            cur_index = list1.index(rest) + list2.index(rest)
            if cur_index < min_index:
                min_index, result = cur_index, [rest]
            elif cur_index == min_index:
                result.append(rest)
        return result
