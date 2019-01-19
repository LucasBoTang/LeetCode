# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        cur_count = max_count = 0
        cur_num = ''
        for num in self.traverseInOrder(root):
            if num == cur_num:
                cur_count += 1
            else:
                cur_count = 1
                cur_num = num
            if cur_count > max_count:
                max_count = cur_count
                result = [num]
            elif cur_count == max_count:
                result.append(num)
        return result

    def traverseInOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        if root.left:
            result += self.traverseInOrder(root.left)
        result += [root.val]
        if root.right:
            result += self.traverseInOrder(root.right)
        return result
