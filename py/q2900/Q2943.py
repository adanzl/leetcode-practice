"""
 * 给你一个网格图，由 n + 2 条 横线段 和 m + 2 条 竖线段 组成，一开始所有区域均为 1 x 1 的单元格。
 * 所有线段的编号从 1 开始。
 * 给你两个整数 n 和 m 。
 * 同时给你两个整数数组 hBars 和 vBars 。
 * 1、hBars 包含区间 [2, n + 1] 内 互不相同 的横线段编号。
 * 2、vBars 包含 [2, m + 1] 内 互不相同的 竖线段编号。
 * 如果满足以下条件之一，你可以 移除 两个数组中的部分线段：
 * 1、如果移除的是横线段，它必须是 hBars 中的值。
 * 2、如果移除的是竖线段，它必须是 vBars 中的值。
 * 请你返回移除一些线段后（可能不移除任何线段），剩余网格图中 最大正方形 空洞的面积，正方形空洞的意思是正方形 内部 不含有任何线段。
 * 提示：
 * 1、1 <= n <= 10^9
 * 2、1 <= m <= 10^9
 * 3、1 <= hBars.length <= 100
 * 4、2 <= hBars[i] <= n + 1
 * 5、1 <= vBars.length <= 100
 * 6、2 <= vBars[i] <= m + 1
 * 7、hBars 中的值互不相同。
 * 8、vBars 中的值互不相同。
 * 链接：https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid/
"""
from typing import List


class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        i_v, i_h =  (2 if vBars else 1), (2 if hBars else 1)
        ans_v, ans_h = i_v, i_h
        hh = ans_h
        for i in range(1, len(hBars)):
            if hBars[i] == n + 2: continue
            if hBars[i] == hBars[i - 1] + 1:
                hh += 1
                ans_h = max(ans_h, hh)
            else:
                hh = i_h
        vv = ans_v
        for i in range(1, len(vBars)):
            if vBars[i] == m + 2: continue
            if vBars[i] == vBars[i - 1] + 1:
                vv += 1
                ans_v = max(ans_v, vv)
            else:
                vv = i_v
        return min(ans_v, ans_h)**2


if __name__ == '__main__':
    # 9
    print(Solution().maximizeSquareHoleArea(3, m=13, hBars=[2, 4, 3], vBars=[4, 6, 7, 12, 10, 13, 2]))
    # 9
    print(Solution().maximizeSquareHoleArea(2, m=3, hBars=[2, 3], vBars=[2, 3, 4]))
    # 9
    print(Solution().maximizeSquareHoleArea(4, m=40, hBars=[5, 3, 2, 4], vBars=[36, 41, 6, 34, 33]))
    # 4
    print(Solution().maximizeSquareHoleArea(2, m=1, hBars=[2, 3], vBars=[2]))
    # 4
    print(Solution().maximizeSquareHoleArea(1, m=1, hBars=[2], vBars=[2]))
