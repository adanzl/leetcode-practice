"""
 * 给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。
 * 你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，并满足 i0 < i1 < i2 < i3。
 * 你的得分将是 a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。
 * 返回你能够获得的 最大 得分。
 * 提示：
 * 1、a.length == 4
 * 2、4 <= b.length <= 10^5
 * 3、-10^5 <= a[i], b[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-multiplication-score/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        f = [[-INF] * (n + 1) for _ in range(len(a) + 1)]
        for i in range(n + 1):
            f[0][i] = 0
        for i0, v0 in enumerate(a):
            for i1 in range(i0, n):
                f[i0 + 1][i1 + 1] = max(f[i0 + 1][i1], f[i0][i1] + b[i1] * v0)
        return f[-1][-1]


if __name__ == '__main__':
    # 26
    print(Solution().maxScore([3, 2, 5, 6], b=[2, -6, 4, -5, -3, 2, -7]))
    # -1
    print(Solution().maxScore([-1, 4, 5, -2], b=[-5, -1, -3, -2, -4]))
