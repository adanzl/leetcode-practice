"""
 * 给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。
 * 你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：
 * 从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。
 * 返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。
 * 注意：
 * 1、查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。
 * 2、树的高度是从根到树中某个节点的 最长简单路径中的边数 。
 * 提示：
 * 1、树中节点的数目是 n
 * 2、2 <= n <= 10^5
 * 3、1 <= Node.val <= n
 * 4、树中的所有值 互不相同
 * 5、m == queries.length
 * 6、1 <= m <= min(n, 10^4)
 * 7、1 <= queries[i] <= n
 * 8、queries[i] != root.val
 * 链接：https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/
"""
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_map = dict()

        def get_height(node):
            if node is None: return 0
            node.l = get_height(node.left)
            node.r = get_height(node.right)
            node.d = max(node.l, node.r) + 1
            node_map[node.val] = node
            return node.d

        get_height(root)

        def dfs(node, deep, max_depth):
            if node is None: return
            node.dd = max_depth
            deep += 1
            dfs(node.left, deep, max(max_depth, node.r + deep))
            dfs(node.right, deep, max(max_depth, node.l + deep))

        dfs(root, -1, 0)
        return [node_map[q].dd for q in queries]


if __name__ == '__main__':
    # [3,2,3,2]
    print(Solution().treeQueries(stringToTreeNode("[5,8,9,2,1,3,7,4,6]"), [3, 2, 4, 8]))
    # [1, 0, 3, 3, 3]
    print(Solution().treeQueries(stringToTreeNode("[1,null,5,3,null,2,4]"), [3, 5, 4, 2, 4]))
    # [2]
    print(Solution().treeQueries(stringToTreeNode("[1,3,4,2,null,6,5,null,null,null,null,null,7]"), [4]))
