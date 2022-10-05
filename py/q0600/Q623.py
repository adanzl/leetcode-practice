"""
 * 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
 * 注意，根节点 root 位于深度 1 。
 * 加法规则如下:
 * 1、给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
 * 2、cur 原来的左子树应该是新的左子树根的左子树。
 * 3、cur 原来的右子树应该是新的右子树根的右子树。
 * 4、如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。
 * 提示:
 * 1、节点数在 [1, 10^4] 范围内
 * 2、树的深度在 [1, 10^4]范围内
 * 3、-100 <= Node.val <= 100
 * 4、-10^5 <= val <= 10^5
 * 5、1 <= depth <= the depth of tree + 1
 * 链接：https://leetcode.cn/problems/add-one-row-to-tree/
"""
from typing import *
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(root, d):
            if root is None: return root
            if d == depth - 1:
                root.left = TreeNode(val, root.left)
                root.right = TreeNode(val, None, root.right)
                return
            dfs(root.left, d + 1)
            dfs(root.right, d + 1)

        h = TreeNode()
        h.left = root
        dfs(h, 0)
        return h.left


if __name__ == '__main__':
    # [1,4,null,2,6,3,1,5]
    print(Solution().addOneRow(stringToTreeNode("[4,2,6,3,1,5]"), 1, 1))
    # [1,2,3,4,null,null,null,5,5]
    print(Solution().addOneRow(stringToTreeNode("[1,2,3,4]"), 5, 4))
    # [4,1,1,2,null,null,6,3,1,5]
    print(Solution().addOneRow(stringToTreeNode("[4,2,6,3,1,5]"), 1, 2))
    # [4,2,null,1,1,3,null,null,1]
    print(Solution().addOneRow(stringToTreeNode("[4,2,null,3,1]"), 1, 3))
