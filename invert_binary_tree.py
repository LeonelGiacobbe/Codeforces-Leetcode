"""
Link: https://leetcode.com/problems/invert-binary-tree/
Language: Python
Topics: Recursion
Keys to solve: 
- Swap of values using a temporary variable
- DONT FORGET base case for recursion 
- Technically executing Pre-Order Traversal
"""


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if(root == None):

            return

        else:

            tmp = root.left

            root.left = root.right

            root.right = tmp

            root.left, root.right = root.right, root.left

            self.invertTree(root.left)

            self.invertTree(root.right)

  

        return root