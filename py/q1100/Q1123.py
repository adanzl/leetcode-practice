"""
 * 给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。
 * 回想一下：
 * 1、叶节点 是二叉树中没有子节点的节点
 * 2、树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
 * 3、如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
 * 提示：
 * 1、树中的节点数将在 [1, 1000] 的范围内。
 * 2、0 <= Node.val <= 1000
 * 3、每个节点的值都是 独一无二 的。
 * 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root, depth):  # node, depth
            if not root: return depth - 1, root
            dl, l = dfs(root.left, depth + 1)
            dr, r = dfs(root.right, depth + 1)
            if dl == dr: return dl, root
            if dl > dr: return dl, l
            return dr, r

        return dfs(root, 0)[1]


if __name__ == '__main__':
    # [2,7,4]
    print(Solution().lcaDeepestLeaves(stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")))
    # [1]
    print(Solution().lcaDeepestLeaves(stringToTreeNode("[1]")))
    # [2]
    print(Solution().lcaDeepestLeaves(stringToTreeNode("[0,1,3,null,2]")))