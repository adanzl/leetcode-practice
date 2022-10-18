"""
 * 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
 * 1、每个节点都有 0 个或是 2 个子节点。
 * 2、数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
 * 3、每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
 * 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
 * 提示：
 * 1、2 <= arr.length <= 40
 * 2、1 <= arr[i] <= 15
 * 3、答案保证是一个 32 位带符号整数，即小于 2^31。
 * 链接：https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/
"""
from typing import List


class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        inf = 0x3c3c3c3c

        mx = [[0] * n for i in range(n)]
        for i in range(n):
            mx[i][i] = arr[i]
            for j in range(i + 1, n):
                mx[i][j] = max(mx[i][j - 1], arr[j])

        dp = [[inf] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 0
            for j in range(i - 1, -1, -1):
                for k in range(j, i):
                    dp[j][i] = min(dp[j][i], dp[j][k] + dp[k + 1][i] + mx[j][k] * mx[k + 1][i])
        return dp[0][-1]


if __name__ == '__main__':
    # 32
    print(Solution().mctFromLeafValues([6, 2, 4]))
    # 44
    print(Solution().mctFromLeafValues([4, 11]))
