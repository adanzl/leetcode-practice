from collections import deque
"""
 * 给定一个二维网格 grid ，其中：
 * 1、'.' 代表一个空房间
 * 2、'#' 代表一堵
 * 3、'@' 是起点
 * 4、小写字母代表钥匙
 * 5、大写字母代表锁
 * 我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。
 * 除非我们手里有对应的钥匙，否则无法通过锁。假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，字母表中的前 k 个字母在网格中都有自己对应的一个小写和一个大写字母。
 * 换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。
 * 返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 30
 * 4、grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
 * 5、钥匙的数目范围是 [1, 6] 
 * 6、每个钥匙都对应一个 不同 的字母
 * 7、每个钥匙正好打开一个对应的锁
 * 链接：https://leetcode.cn/problems/shortest-path-to-get-all-keys
"""


class Solution:

    def shortestPathAllKeys(self, grid: list[str]) -> int:
        q = deque()
        dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        m, n, nk = len(grid), len(grid[0]), 0
        start = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'f' >= grid[i][j] >= 'a':
                    nk += 1
        q.append(start)
        ans = 0
        visited, keys, locked = set(), set(), set()
        visited.add(start)
        while len(q) > len(locked):
            size = len(q)
            print(list(q))
            for _ in range(size):
                x, y = q.popleft()
                if 'F' >= grid[x][y] >= 'A':
                    if grid[x][y].lower() not in keys:
                        q.append([x, y])
                        locked.add(grid[x][y].lower())
                        continue
                for d in dir:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == '#':
                        continue
                    if (nx, ny) in visited:
                        continue
                    if 'f' >= grid[nx][ny] >= 'a':
                        keys.add(grid[nx][ny])
                        locked.discard(grid[nx][ny])
                        if len(keys) == nk:
                            return ans + 1
                    visited.add((nx, ny))
                    q.append([nx, ny])
            ans += 1
            pass
        return -1


if __name__ == '__main__':
    # print(Solution().shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"]))
    print(Solution().shortestPathAllKeys(["@...a", ".###A", "b.BCc"]))
