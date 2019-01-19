class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)



    def isSameTree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s and not t:
            return True

        if not s or not t:
            return False

        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
