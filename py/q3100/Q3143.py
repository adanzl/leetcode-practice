"""
 * 给你一个二维数组 points 和一个字符串 s ，其中 points[i] 表示第 i 个点的坐标，s[i] 表示第 i 个点的 标签 。
 * 如果一个正方形的中心在 (0, 0) ，所有边都平行于坐标轴，且正方形内 不 存在标签相同的两个点，那么我们称这个正方形是 合法 的。
 * 请你返回 合法 正方形中可以包含的 最多 点数。
 * 注意：
 * 1、如果一个点位于正方形的边上或者在边以内，则认为该点位于正方形内。
 * 2、正方形的边长可以为零。
 * 提示：
 * 1、1 <= s.length, points.length <= 10^5
 * 2、points[i].length == 2
 * 3、-10^9 <= points[i][0], points[i][1] <= 10^9
 * 4、s.length == points.length
 * 5、points 中的点坐标互不相同。
 * 6、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/maximum-points-inside-the-square/
"""
from typing import List


class Solution:

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        arr = sorted([[x, y, i] for i, (x, y) in enumerate(points)], key=lambda x: max(abs(x[0]), abs(x[1])))
        n = len(arr)
        ss = set()
        ans, ii = 0, 0
        while ii < n:
            ln = max(abs(arr[ii][0]), abs(arr[ii][1]))
            if s[arr[ii][2]] in ss:
                break
            ss.add(s[arr[ii][2]])
            ii += 1
            val, f = 1, True
            while ii < n and max(abs(arr[ii][0]), abs(arr[ii][1])) <= ln:
                if s[arr[ii][2]] not in ss:
                    ss.add(s[arr[ii][2]])
                    val += 1
                else:
                    f = False
                    break
                ii += 1
            if f:
                ans += val
            else:
                break

        return ans


if __name__ == '__main__':
    # 0
    print(Solution().maxPointsInsideSquare([[1, 1], [-1, -1], [2, -2]], s="ccd"))
    # 2
    print(Solution().maxPointsInsideSquare([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"))
    # 1
    print(Solution().maxPointsInsideSquare([[1, 1], [-2, -2], [-2, 2]], s="abb"))
