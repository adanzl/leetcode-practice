"""
 * 给你一个 n x n 的二维数组 grid，它包含范围 [0, n2 - 1] 内的不重复元素。
 * 实现 neighborSum 类：
 * 1、neighborSum(int [][]grid) 初始化对象。
 * 2、int adjacentSum(int value) 返回在 grid 中与 value 相邻的元素之和，相邻指的是与 value 在上、左、右或下的元素。
 * 3、int diagonalSum(int value) 返回在 grid 中与 value 对角线相邻的元素之和，对角线相邻指的是与 value 在左上、右上、左下或右下的元素。
 * 提示：
 * 1、3 <= n == grid.length == grid[0].length <= 10
 * 2、0 <= grid[i][j] <= n2 - 1
 * 3、所有 grid[i][j] 值均不重复。
 * 4、adjacentSum 和 diagonalSum 中的 value 均在范围 [0, n^2 - 1] 内。
 * 5、最多会调用 adjacentSum 和 diagonalSum 总共 2 * n^2 次。
 * 链接：https://leetcode.cn/problems/design-neighbor-sum-service/
"""
from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.idx = {}
        self.n = len(grid)
        self.grid = grid
        for i in range(self.n):
            for j in range(self.n):
                self.idx[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.idx[value]
        ans = 0
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= self.n or ny < 0 or ny >= self.n:
                continue
            ans += self.grid[nx][ny]
        return ans

    def diagonalSum(self, value: int) -> int:
        i, j = self.idx[value]
        ans = 0
        for dx, dy in [[1, 1], [-1, -1], [1, -1], [-1, 1]]:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= self.n or ny < 0 or ny >= self.n:
                continue
            ans += self.grid[nx][ny]
        return ans


if __name__ == '__main__':
    obj = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    # 6
    print(obj.adjacentSum(1))
    # 16
    print(obj.adjacentSum(4))
    # 16
    print(obj.diagonalSum(4))
    # 4
    print(obj.diagonalSum(8))
