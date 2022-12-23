"""
 * 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
 * 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和 bi的人归入同一组。
 * 当可以用这种方法将所有人分进两组时，返回 true; 否则返回 false。
 * 提示：
 * 1、1 <= n <= 2000
 * 2、0 <= dislikes.length <= 10^4
 * 3、dislikes[i].length == 2
 * 4、1 <= dislikes[i][j] <= n
 * 5、ai < bi
 * 6、dislikes 中每一组都 不同
 * 链接：https://leetcode-cn.com/problems/possible-bipartition
"""
from typing import List


class Solution:
    # 「染色法判定二分图」的模板题
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for i in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        colors = [0] * n

        def dfs(idx, color):
            if colors[idx] != 0: return colors[idx] == color
            colors[idx] = color
            return all([dfs(nx, 1 if color == 2 else 2) for nx in g[idx]])

        return all([dfs(i, 1) for i in range(n) if colors[i] == 0])


if __name__ == '__main__':
    # True
    print(Solution().possibleBipartition(4, dislikes=[[1, 2], [1, 3], [2, 4]]))
    # False
    print(Solution().possibleBipartition(3, dislikes=[[1, 2], [1, 3], [2, 3]]))
    # False
    print(Solution().possibleBipartition(5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
