"""
 * 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。
 * 只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true 否则返回 false。
 * 如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。
 * 注意：节点没有值，本问题中仅仅使用节点编号。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、leftChild.length == rightChild.length == n
 * 3、-1 <= leftChild[i], rightChild[i] <= n - 1
 * 链接：https://leetcode.cn/problems/validate-binary-tree-nodes/
"""

import re
from typing import List

#
# @lc app=leetcode.cn id=1361 lang=python3
#
# [1361] 验证二叉树
#


# @lc code=start
class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [i for i in range(n)]
        cnt = 0

        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]

        in_d = [0] * n
        for i, (vl, vr) in enumerate(zip(leftChild, rightChild)):
            r0 = find(i)
            if vl != -1:
                in_d[vl] += 1
                r1 = find(vl)
                if r0 != r1:
                    cnt += 1
                    parent[r1] = r0
                else:
                    return False
            if vr != -1:
                in_d[vr] += 1
                r2 = find(vr)
                if r0 != r2:
                    cnt += 1
                    parent[r2] = r0
                else:
                    return False
        return cnt == n - 1 and sum([1 for v in in_d if v == 0]) == 1


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().validateBinaryTreeNodes(4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
    # False
    print(Solution().validateBinaryTreeNodes(4, leftChild=[1, 0, 3, -1], rightChild=[-1, -1, -1, -1]))
    # False
    print(Solution().validateBinaryTreeNodes(4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
    # False
    print(Solution().validateBinaryTreeNodes(2, leftChild=[1, 0], rightChild=[-1, -1]))
    # False
    print(Solution().validateBinaryTreeNodes(6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
