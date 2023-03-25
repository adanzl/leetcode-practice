"""
 * 有一个无穷大的二维网格图，一开始所有格子都未染色。给你一个正整数 n ，表示你需要执行以下步骤 n 分钟：
 * 1、第一分钟，将 任一 格子染成蓝色。
 * 2、之后的每一分钟，将与蓝色格子相邻的 所有 未染色格子染成蓝色。
 * 下图分别是 1、2、3 分钟后的网格图。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/count-total-number-of-colored-cells/
"""


class Solution:

    def coloredCells(self, n: int) -> int:
        return 1 + (1 + n - 1) * (n - 1) // 2 * 4


if __name__ == '__main__':
    # 1
    print(Solution().coloredCells(1))
    # 5
    print(Solution().coloredCells(2))