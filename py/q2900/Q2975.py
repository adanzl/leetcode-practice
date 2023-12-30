"""
 * 有一个大型的 (m - 1) x (n - 1) 矩形田地，其两个对角分别是 (1, 1) 和 (m, n) ，
 * 田地内部有一些水平栅栏和垂直栅栏，分别由数组 hFences 和 vFences 给出。
 * 水平栅栏为坐标 (hFences[i], 1) 到 (hFences[i], n)，垂直栅栏为坐标 (1, vFences[i]) 到 (m, vFences[i]) 。
 * 返回通过 移除 一些栅栏（可能不移除）所能形成的最大面积的 正方形 田地的面积，或者如果无法形成正方形田地则返回 -1。
 * 由于答案可能很大，所以请返回结果对 10^9 + 7 取余 后的值。
 * 注意：田地外围两个水平栅栏（坐标 (1, 1) 到 (1, n) 和坐标 (m, 1) 到 (m, n) ）以及两个垂直栅栏（坐标 (1, 1) 到 (m, 1) 和坐标 (1, n) 到 (m, n) ）所包围。
 * 这些栅栏 不能 被移除。
 * 提示：
 * 1、3 <= m, n <= 10^9
 * 2、1 <= hFences.length, vFences.length <= 600
 * 3、1 < hFences[i] < m
 * 4、1 < vFences[i] < n
 * 5、hFences 和 vFences 中的元素是唯一的。
 * 链接：https://leetcode.cn/problems/maximum-square-area-by-removing-fences-from-a-field/
"""
from typing import List


class Solution:

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        v, h = set([n - 1]), set([m - 1])
        vs, hs = [1], [1]
        for vv in sorted(vFences):
            for p in vs:
                v.add(vv - p)
            vs.append(vv)
            v.add(n - vv)
        for hh in sorted(hFences):
            for p in hs:
                h.add(hh - p)
            hs.append(hh)
            h.add(m - hh)
        ans = -1
        for v1 in v:
            if v1 in h:
                ans = max(ans, v1)
        return ans * ans % (10**9 + 7) if ans != -1 else -1


if __name__ == '__main__':
    # 4
    print(Solution().maximizeSquareArea(3, 9, [2], [8, 6, 5, 4]))
    # -1
    print(Solution().maximizeSquareArea(6, 7, [2], [4]))
    # 4
    print(Solution().maximizeSquareArea(4, n=3, hFences=[2, 3], vFences=[2]))
    # -1
    print(Solution().maximizeSquareArea(6, n=7, hFences=[2], vFences=[4]))
