class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t:
            return str(t.val) + self.dfs(t)
        else:
            return ''



    def dfs(self, node):
        """
        :type t: TreeNode
        :rtype: str
        """

        result = ''

        if node.left:
            result += '('
            result += str(node.left.val)
            result += self.dfs(node.left)
            result += ')'
        elif node.right:
            result += '()'

        if node.right:
            result += '('
            result += str(node.right.val)
            result += self.dfs(node.right)
            result += ')'

        return result
