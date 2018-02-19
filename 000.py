# C:\Users\Apocrypse\OneDrive\Study\Python\LeetCode
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
a1 = TreeNode(1)
b1 = TreeNode(1)
b2 = TreeNode(2)
c1 = TreeNode(2)
c2 = TreeNode(None)
c3 = TreeNode(3)
c4 = TreeNode(5)

a1.left = b1
a1.right = b2
b1.left = c1
b1.right = c2
b2.left = c3
b2.right = c4

print(__init__(a1.right))
