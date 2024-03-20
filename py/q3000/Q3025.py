"""
 * 给你一个  n x 2 的二维数组 points ，它表示二维平面上的一些点坐标，其中 points[i] = [xi, yi] 。
 * 我们定义 x 轴的正方向为 右 （x 轴递增的方向），x 轴的负方向为 左 （x 轴递减的方向）。类似的，我们定义 y 轴的正方向为 上 （y 轴递增的方向），y 轴的负方向为 下 （y 轴递减的方向）。
 * 你需要安排这 n 个人的站位，这 n 个人中包括 liupengsay 和小羊肖恩 。你需要确保每个点处 恰好 有 一个 人。同时，liupengsay 想跟小羊肖恩单独玩耍，所以 liupengsay 会以 liupengsay 的坐标为 左上角 ，小羊肖恩的坐标为 右下角 建立一个矩形的围栏（注意，围栏可能 不 包含任何区域，也就是说围栏可能是一条线段）。如果围栏的 内部 或者 边缘 上有任何其他人，liupengsay 都会难过。
 * 请你在确保 liupengsay 不会 难过的前提下，返回 liupengsay 和小羊肖恩可以选择的 点对 数目。
 * 注意，liupengsay 建立的围栏必须确保 liupengsay 的位置是矩形的左上角，小羊肖恩的位置是矩形的右下角。比方说，以 (1, 1) ，(1, 3) ，(3, 1) 和 (3, 3) 为矩形的四个角，给定下图的两个输入，liupengsay 都不能建立围栏，原因如下：
 * 1、图一中，liupengsay 在 (3, 3) 且小羊肖恩在 (1, 1) ，liupengsay 的位置不是左上角且小羊肖恩的位置不是右下角。
 * 2、图二中，liupengsay 在 (1, 3) 且小羊肖恩在 (1, 1) ，小羊肖恩的位置不是在围栏的右下角。
 * 提示：
 * 1、2 <= n <= 50
 * 2、points[i].length == 2
 * 3、0 <= points[i][0], points[i][1] <= 50
 * 4、points[i] 点对两两不同。
 * 链接：https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-i/description/
"""
from typing import List


class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        s = set([(x, y) for x, y in points])
        ans = 0
        n = len(points)
        for i, (x, y) in enumerate(points):
            for j in range(n):
                if i == j: continue
                px, py = points[j]
                if px > x or py < y:
                    continue
                fit = True
                for ix in range(min(x, px), max(x, px) + 1):
                    for iy in range(min(y, py), max(y, py) + 1):
                        if (ix == x and iy == y) or (ix == px and iy == py):
                            continue
                        if (ix, iy) in s:
                            fit = False
                            break
                if fit:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]))
    # 2
    print(Solution().numberOfPairs([[0, 1], [1, 3], [6, 1]]))
    # 0
    print(Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]))
    # 2
    print(Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]))
