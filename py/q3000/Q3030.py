"""
 * 给你一个下标从 0 开始、大小为 m x n 的网格 image ，表示一个灰度图像，其中 image[i][j] 表示在范围 [0..255] 内的某个像素强度。
 * 另给你一个 非负 整数 threshold 。
 * 如果 image[a][b] 和 image[c][d] 满足 |a - c| + |b - d| == 1 ，则称这两个像素是 相邻像素 。
 * 区域 是一个 3 x 3 的子网格，且满足区域中任意两个 相邻 像素之间，像素强度的 绝对差 小于或等于 threshold 。
 * 区域 内的所有像素都认为属于该区域，而一个像素 可以 属于 多个 区域。
 * 你需要计算一个下标从 0 开始、大小为 m x n 的网格 result ，
 * 其中 result[i][j] 是 image[i][j] 所属区域的 平均 强度，向下取整 到最接近的整数。
 * 如果 image[i][j] 属于多个区域，result[i][j] 是这些区域的 “取整后的平均强度” 的 平均值，也 向下取整 到最接近的整数。
 * 如果 image[i][j] 不属于任何区域，则 result[i][j] 等于 image[i][j] 。
 * 返回网格 result 。
 * 提示：
 * 1、3 <= n, m <= 500
 * 2、0 <= image[i][j] <= 255
 * 3、0 <= threshold <= 255
 * 链接：https://leetcode.cn/problems/find-the-grid-of-region-average/
"""
from typing import List


class Solution:

    def resultGrid(self, a: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(a), len(a[0])
        result = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]
        for i in range(2, m):
            for j in range(2, n):
                # 检查左右相邻格子
                ok = True
                for row in a[i - 2:i + 1]:
                    if abs(row[j - 2] - row[j - 1]) > threshold or abs(row[j - 1] - row[j]) > threshold:
                        ok = False
                        break  # 不合法，下一个
                if not ok: continue

                # 检查上下相邻格子
                for y in range(j - 2, j + 1):
                    if abs(a[i - 2][y] - a[i - 1][y]) > threshold or abs(a[i - 1][y] - a[i][y]) > threshold:
                        ok = False
                        break  # 不合法，下一个
                if not ok: continue

                # 合法，计算 3x3 子网格的平均值
                avg = sum(a[x][y] for x in range(i - 2, i + 1) for y in range(j - 2, j + 1)) // 9

                # 更新 3x3 子网格内的 result
                for x in range(i - 2, i + 1):
                    for y in range(j - 2, j + 1):
                        result[x][y] += avg  # 先累加，最后再求平均值
                        cnt[x][y] += 1

        for i, row in enumerate(cnt):
            for j, c in enumerate(row):
                if c == 0:  # (i,j) 不属于任何子网格
                    result[i][j] = a[i][j]
                else:
                    result[i][j] //= c  # 求平均值
        return result


if __name__ == '__main__':
    # [[9,9,9,9],[9,9,9,9],[9,9,9,9]]
    print(Solution().resultGrid([[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], threshold=3))
    # [[25,25,25],[27,27,27],[27,27,27],[30,30,30]]
    print(Solution().resultGrid([[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], threshold=12))
    # [[5,6,7],[8,9,10],[11,12,13]]
    print(Solution().resultGrid([[5, 6, 7], [8, 9, 10], [11, 12, 13]], threshold=1))
