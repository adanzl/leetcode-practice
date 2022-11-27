"""
 * 圆内一个 有效切割 ，符合以下二者之一：
 * 1、该切割是两个端点在圆上的线段，且该线段经过圆心。
 * 2、该切割是一端在圆心另一端在圆上的线段。
 * 一些有效和无效的切割如下图所示。
 * 给你一个整数 n ，请你返回将圆切割成相等的 n 等分的 最少 切割次数。
 * 提示：1 <= n <= 100
 * 链接：https://leetcode.cn/problems/minimum-cuts-to-divide-a-circle/
"""


class Solution:

    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        return n // 2 if n % 2 == 0 else n


if __name__ == '__main__':
    # 2
    print(Solution().numberOfCuts(4))
    # 3
    print(Solution().numberOfCuts(3))