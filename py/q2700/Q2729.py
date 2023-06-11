"""
 * 给你一个三位数整数 n 。
 * 如果经过以下修改得到的数字 恰好 包含数字 1 到 9 各一次且不包含任何 0 ，那么我们称数字 n 是 迷人的 ：
 * 将 n 与数字 2 * n 和 3 * n 连接 。
 * 如果 n 是迷人的，返回 true，否则返回 false 。
 * 连接 两个数字表示把它们首尾相接连在一起。比方说 121 和 371 连接得到 121371 。
 * 提示：100 <= n <= 999
 * 链接：https://leetcode.cn/problems/check-if-the-number-is-fascinating/
"""


class Solution:

    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(n * 2) + str(n * 3)
        return set(s) == set('123456789') and len(s) == 9


if __name__ == '__main__':
    # True
    print(Solution().isFascinating(192))
    # False
    print(Solution().isFascinating(100))
    # False
    print(Solution().isFascinating(783))