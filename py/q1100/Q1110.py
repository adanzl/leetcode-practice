"""
 * 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
 * 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
 * 返回森林中的每棵树。你可以按任意顺序组织答案。
 * 提示：
 * 1、树中的节点数最大为 1000。
 * 2、每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
 * 3、to_delete.length <= 1000
 * 4、to_delete 包含一些从 1 到 1000、各不相同的值。
 * 链接：https://leetcode.cn/problems/delete-nodes-and-return-forest/
"""
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []

        def func(root, new):
            if root is None: return None
            d = root.val in to_delete
            root.left = func(root.left, d)
            root.right = func(root.right, d)
            if new and not d:
                ans.append(root)
            return None if d else root

        func(root, True)
        return ans


if __name__ == '__main__':
    #
    print(Solution().delNodes(stringToTreeNode('[1, 2, 3, 4, 5, 6, 7]'), to_delete=[3, 5]))
    #
    print(Solution().delNodes(stringToTreeNode('[1,2,4,null,3]'), [3]))