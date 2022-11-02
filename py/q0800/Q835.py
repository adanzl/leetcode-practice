"""
 * 给你两个图像 img1 和 img2 ，两个图像的大小都是 n x n ，用大小相同的二进制正方形矩阵表示。二进制矩阵仅由若干 0 和若干 1 组成。
 * 转换 其中一个图像，将所有的 1 向左，右，上，或下滑动任何数量的单位；然后把它放在另一个图像的上面。该转换的 重叠 是指两个图像 都 具有 1 的位置的数目。
 * 请注意，转换 不包括 向任何方向旋转。越过矩阵边界的 1 都将被清除。
 * 最大可能的重叠数量是多少？
 * 提示：
 * 1、n == img1.length == img1[i].length
 * 2、n == img2.length == img2[i].length
 * 3、1 <= n <= 30
 * 4、img1[i][j] 为 0 或 1
 * 5、img2[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/image-overlap/
"""
from typing import List


class Solution:

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        mark1, mark2 = [0] * n, [0] * n
        for i in range(n):
            for j in range(n):
                if img1[i][j]: mark1[i] |= 1 << (n - 1 - j)
                if img2[i][j]: mark2[i] |= 1 << (n - 1 - j)
        ans = 0

        def f(m1, m2, dx, dy):  # move m1 and merge with m2
            ret = 0
            for i in range(max(0, dx), min(n, n + dx)):
                num = m2[i] & ((m1[i - dx] >> dy) if dy >= 0 else (m1[i - dx] << -dy))
                ret += num.bit_count()
            return ret

        for i in range(1 - n, n):
            for j in range(1 - n, n):
                ans = max(ans, f(mark1, mark2, i, j))
                ans = max(ans, f(mark2, mark1, i, j))
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
    # 1
    print(Solution().largestOverlap([[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                                    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]))
    # 1
    print(Solution().largestOverlap([[1]], [[1]]))
    # 0
    print(Solution().largestOverlap([[0]], [[0]]))
