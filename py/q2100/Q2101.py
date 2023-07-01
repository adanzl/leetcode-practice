"""
 * 给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。
 * 炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。
 * 你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。
 * 给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。
 * 提示：
 * 1、1 <= bombs.length <= 100
 * 2、bombs[i].length == 3
 * 3、1 <= xi, yi, ri <= 10^5
 * 链接：https://leetcode.cn/problems/detonate-the-maximum-bombs/
"""
from typing import List


class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]

        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i == j: continue
                if (xi - xj)**2 + (yi - yj)**2 <= ri**2:
                    g[i].append(j)
        dis = [1] * n
        for i, (xi, yi, ri) in enumerate(bombs):
            q = [i]
            vis = {i}
            while q:
                t = []
                for idx in q:
                    for nx in g[idx]:
                        if nx in vis: continue
                        vis.add(nx)
                        dis[i] += 1
                        t.append(nx)
                q = t

        return max(dis)


if __name__ == '__main__':
    # 9
    print(Solution().maximumDetonation([[855, 82, 158], [17, 719, 430], [90, 756, 164], [376, 17, 340], [691, 636, 152], [565, 776, 5], [464, 154, 271], [53, 361, 162], [278, 609, 82],
                                        [202, 927, 219], [542, 865, 377], [330, 402, 270], [720, 199, 10], [986, 697, 443], [471, 296, 69], [393, 81, 404], [127, 405, 177]]))
    # 2
    print(Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]]))
    # 1
    print(Solution().maximumDetonation([[1, 1, 5], [10, 10, 5]]))
    # 5
    print(Solution().maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
