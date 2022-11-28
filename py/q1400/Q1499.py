"""
 * 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。
 * 也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
 * 请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
 * 题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。
 * 提示：
 * 1、2 <= points.length <= 10^5
 * 2、points[i].length == 2
 * 3、-10^8 <= points[i][0], points[i][1] <= 10^8
 * 4、0 <= k <= 2 * 10^8
 * 5、对于所有的1 <= i < j <= points.length ，points[i][0] < points[j][0] 都成立。也就是说，xi 是严格递增的。
 * 链接：https://leetcode.cn/problems/max-value-of-equation/
"""
from typing import List, Deque


class Solution:

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # y-x
        q = Deque()
        ans = -0x3c3c3c3c
        for i, (x, y) in enumerate(points):
            while q and x - points[q[0]][0] > k:
                q.popleft()
            if q: ans = max(ans, y + points[q[0]][1] + x - points[q[0]][0])
            while q and points[q[-1]][1] - points[q[-1]][0] < y - x:
                q.pop()
            q.append(i)
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().findMaxValueOfEquation([[-18, -4], [-16, -20], [-13, -1], [-7, 10], [-2, -2], [-1, -5], [2, 11], [5, -10], [9, 0], [10, 10], [12, 2], [17, -5]], 6))
    # 35
    print(Solution().findMaxValueOfEquation([[-19, -12], [-13, -18], [-12, 18], [-11, -8], [-8, 2], [-7, 12], [-5, 16], [-3, 9], [1, -7], [5, -4], [6, -20], [10, 4], [16, 4], [19, -9], [20, 19]], 6))
    # 4
    print(Solution().findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))
    # 3
    print(Solution().findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], k=3))
