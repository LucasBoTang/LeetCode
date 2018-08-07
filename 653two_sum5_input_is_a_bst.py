class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        queue = [root]
        hash_lst = []

        while queue:
            new_queue = []

            for node in queue:
                if k - node.val in hash_lst:
                    return True
                hash_lst.append(node.val)

                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            queue = new_queue

        return False
