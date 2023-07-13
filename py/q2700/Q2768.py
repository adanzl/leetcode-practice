"""
 * 给你两个整数 m 和 n ，表示一个下标从 0 开始的 m x n 的网格图。
 * 给你一个下标从 0 开始的二维整数矩阵 coordinates ，其中 coordinates[i] = [x, y] 表示坐标为 [x, y] 的格子是 黑色的 ，所有没出现在 coordinates 中的格子都是 白色的。
 * 一个块定义为网格图中 2 x 2 的一个子矩阵。更正式的，对于左上角格子为 [x, y] 的块，其中 0 <= x < m - 1 且 0 <= y < n - 1 ，包含坐标为 [x, y] ，[x + 1, y] ，[x, y + 1] 和 [x + 1, y + 1] 的格子。
 * 请你返回一个下标从 0 开始长度为 5 的整数数组 arr ，arr[i] 表示恰好包含 i 个 黑色 格子的块的数目。
 * 提示：
 * 1、2 <= m <= 10^5
 * 2、2 <= n <= 10^5
 * 3、0 <= coordinates.length <= 10^4
 * 4、coordinates[i].length == 2
 * 5、0 <= coordinates[i][0] < m
 * 6、0 <= coordinates[i][1] < n
 * 7、coordinates 中的坐标对两两互不相同。
 * 链接：https://leetcode.cn/problems/number-of-black-blocks/
"""
from typing import List


class Solution:

    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        s = set([(x, y) for x, y in coordinates])
        ans = [(m - 1) * (n - 1), 0, 0, 0, 0]

        for x, y in coordinates:
            # 左上角
            if x < m - 1 and y < n - 1:
                c = sum([1 for dx, dy in [(0, 1), (1, 1), (1, 0)] if (x + dx, y + dy) in s]) + 1
                if c:
                    ans[c] += 1
                    ans[0] -= 1
            # 右上角
            if x < m - 1 and y > 0 and (x, y - 1) not in s:
                c = sum([1 for dx, dy in [(1, -1), (1, 0)] if (x + dx, y + dy) in s]) + 1
                if c:
                    ans[c] += 1
                    ans[0] -= 1
            # 左下角
            if x > 0 and y < n - 1 and (x - 1, y) not in s and (x - 1, y + 1) not in s:
                c = sum([1 for dx, dy in [(0, 1)] if (x + dx, y + dy) in s]) + 1
                if c:
                    ans[c] += 1
                    ans[0] -= 1
            # 右下角
            if x > 0 and y > 0 and (x - 1, y) not in s and (x - 1, y - 1) not in s and (x, y - 1) not in s:
                ans[1] += 1
                ans[0] -= 1
        return ans


if __name__ == '__main__':
    # [0,2,2,0,0]
    print(Solution().countBlackBlocks(3, n=3, coordinates=[[0, 0], [1, 1], [0, 2]]))
    # [3,1,0,0,0]
    print(Solution().countBlackBlocks(3, n=3, coordinates=[[0, 0]]))