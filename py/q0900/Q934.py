"""
 * 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
 * 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
 * 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
 * 提示：
 * 1、2 <= A.length == A[0].length <= 100
 * 2、A[i][j] == 0 或 A[i][j] == 1
 * 链接：https://leetcode.cn/problems/shortest-bridge/
"""
from typing import Deque, List


class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = Deque()
        edges = set()
        q.append(next(((i, j) for i in range(m) for j in range(n) if grid[i][j]), -1))
        visited.add(q[0])
        while q:
            size = len(q)
            while size:
                i, j = q.popleft()
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if x < 0 or x > m - 1 or y < 0 or y > n - 1: continue
                    if grid[x][y] == 0:
                        edges.add((i, j))
                        continue
                    if (x, y) in visited: continue
                    visited.add((x, y))
                    q.append((x, y))
                size -= 1
        q = Deque(edges)
        ans = 0
        while q:
            size = len(q)
            while size:
                i, j = q.popleft()
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if x < 0 or x > m - 1 or y < 0 or y > n - 1: continue
                    if (x, y) in visited: continue
                    if grid[x][y] == 1:
                        return ans
                    visited.add((x, y))
                    q.append((x, y))
                size -= 1
            ans += 1
        return -1


if __name__ == '__main__':
    # 2
    print(Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
    # 1
    print(Solution().shortestBridge([[0, 1], [1, 0]]))
    # 1
    print(Solution().shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
