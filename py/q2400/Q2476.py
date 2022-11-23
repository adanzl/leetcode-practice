"""
 * 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。
 * 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：
 * 1、mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
 * 2、maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
 * 返回数组 answer 。
 * 提示：
 * 1、树中节点的数目在范围 [2, 10^5] 内
 * 2、1 <= Node.val <= 10^6
 * 3、n == queries.length
 * 4、1 <= n <= 10^5
 * 5、1 <= queries[i] <= 10^6
 * 链接：https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/
"""
import os
import sys
from bisect import bisect_left, bisect_right
from typing import List

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # 题目没说二叉搜索树是平衡的，最坏情况下二叉搜索树是一条链。
        # 中序遍历再二分查找
        a = []

        def dfs(o: Optional[TreeNode]) -> None:
            if o is None: return
            dfs(o.left)
            a.append(o.val)
            dfs(o.right)

        dfs(root)

        ans = []
        for q in queries:
            j = bisect_right(a, q)
            min = a[j - 1] if j else -1
            j = bisect_left(a, q)
            max = a[j] if j < len(a) else -1
            ans.append([min, max])
        return ans


if __name__ == '__main__':
    # [[2,2],[4,6],[15,-1]]
    print(Solution().closestNodes(stringToTreeNode("[6,2,13,1,4,9,15,null,null,null,null,null,null,14]"), [2, 5, 16]))
    # [[-1,4]]
    print(Solution().closestNodes(stringToTreeNode("[4,null,9]"), [3]))
