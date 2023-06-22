"""
 * 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。
 * 若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
 * 编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
 * 提示：
 * 1、0 < len(land) <= 1000
 * 2、0 < len(land[i]) <= 1000
 * 链接：https://leetcode.cn/problems/pond-sizes-lcci/description/
"""
from typing import List


class Solution:

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(land), len(land[0])
        vis = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if vis[i][j] or land[i][j] != 0: continue
                q = [(i, j)]
                v = 1
                vis[i][j] = True
                while q:
                    t = []
                    for x, y in q:
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and land[nx][ny] == 0:
                                vis[nx][ny] = True
                                t.append((nx, ny))
                                v += 1
                    q = t
                ans.append(v)
        return sorted(ans)


if __name__ == '__main__':
    # [1,2,4]
    print(Solution().pondSizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
    #
    # print(Solution().pondSizes())