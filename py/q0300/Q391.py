"""
 * 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。
 * 这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
 * 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= rectangles.length <= 2 * 10^4
 * 2、rectangles[i].length == 4
 * 3、-10^5 <= xi, yi, ai, bi <= 10^5
 * 链接：https://leetcode.cn/problems/perfect-rectangle
"""

from bisect import bisect_left
from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#


# @lc code=start
class Solution:

    def isRectangleCover1(self, rectangles: List[List[int]]) -> bool:
        # 二维差分，差分是尾部多一个元素，前缀和是头部多一个元素
        arr_x, arr_y = set(), set()
        mn_x, mn_y, mx_x, mx_y = 10**10, 10**10, -10**10, -10**10
        for x, y, a, b in rectangles:
            arr_x.add(x)
            mn_x = min(mn_x, x)
            arr_x.add(x - 1)
            arr_x.add(a - 1)
            mx_x = max(mx_x, a - 1)
            arr_x.add(a)
            arr_y.add(y)
            mn_y = min(mn_y, y)
            arr_y.add(y - 1)
            arr_y.add(b - 1)
            mx_y = max(mx_y, b - 1)
            arr_y.add(b)
        st_x = sorted(arr_x)
        st_y = sorted(arr_y)
        m, n = len(st_y), len(st_x)
        pre_diff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for x, y, a, b in rectangles:
            x1, x2 = bisect_left(st_x, x), bisect_left(st_x, a - 1)  # 离散化坐标
            y1, y2 = bisect_left(st_y, y), bisect_left(st_y, b - 1)
            pre_diff[y1][x1] += 1
            pre_diff[y2 + 1][x2 + 1] += 1
            pre_diff[y1][x2 + 1] -= 1
            pre_diff[y2 + 1][x1] -= 1
        l_sum = [0] * (n + 1)  # 前缀和
        i_s_x, i_s_y = bisect_left(st_x, mn_x), bisect_left(st_y, mn_y)
        i_e_x, i_e_y = bisect_left(st_x, mx_x), bisect_left(st_y, mx_y)
        for i in range(i_s_y, i_e_y + 1):
            n_l_sum = [0] * (n + 1)
            for j in range(i_s_x, i_e_x + 1):
                n_l_sum[j + 1] = n_l_sum[j] + l_sum[j + 1] - l_sum[j] + pre_diff[i][j]
                if n_l_sum[j + 1] != 1:
                    return False
            l_sum = n_l_sum
        return True

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 扫描线解法，所有的矩形都拆解为垂直2条线段，合并线段
        # 左右边缘线段必须只有一段并且长度为最终矩形的高
        # 中间线段必须有两端，且长度相等
        mx_x, mx_y, mn_x, mn_y = -10**10, -10**10, 10**10, 10**10
        seg_l, seg_r = defaultdict(dict), defaultdict(dict)  # y1-y2 矩形左右垂直线段
        area = 0
        for x, y, a, b in rectangles:
            mx_x, mx_y = max(mx_x, a), max(mx_y, b)
            mn_x, mn_y = min(mn_x, x), min(mn_y, y)
            seg_l[x][y] = b
            seg_r[a][y] = b
            area += (a - x) * (b - y)
        if area != (mx_x - mn_x) * (mx_y - mn_y): return False  # 面积不匹配
        # 校验左外垂直线段
        d = seg_l.pop(mn_x, None)
        e = self.merge(d, mn_y)
        if e != mx_y or d: return False
        # 校验右外垂直线段
        d = seg_r.pop(mx_x, None)
        e = self.merge(d, mn_y)
        if e != mx_y or d: return False
        # 校验中间线段
        for k, seg_d_l in seg_l.items():
            seg_d_r = seg_r.get(k, None)
            while seg_d_l:
                start = min(seg_d_l.keys())
                e_l = self.merge(seg_d_l, start)
                e_r = self.merge(seg_d_r, start)
                if e_l != e_r:
                    return False  # 左垂直线段没有找到匹配的右垂直线段
        return True

    def merge(self, seg_dic: dict | None, s):
        if seg_dic is None: return None
        e = s
        while seg_dic and e is not None:
            e = seg_dic.pop(e, None)
        return e


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
    # False
    print(Solution().isRectangleCover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]))
    # False
    print(Solution().isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]))
