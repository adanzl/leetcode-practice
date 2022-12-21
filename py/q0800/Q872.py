"""
 * 链接：https://leetcode.cn/problems/leaf-similar-trees/
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []

        def f(root, arr):
            if root is None: return
            if root.left is None and root.right is None:
                arr.append(root.val)
                return
            f(root.left, arr)
            f(root.right, arr)

        f(root1, arr1)
        f(root2, arr2)
        return arr1 == arr2


if __name__ == '__main__':
    # True
    print(Solution().leafSimilar(
        stringToTreeNode("[3,5,1,6,2,9,8,null,null,7,4]"),
        stringToTreeNode("[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]")))
    # False
    print(Solution().leafSimilar(
        stringToTreeNode("[1,2,3]"),
        stringToTreeNode("[1,3,2]")))
