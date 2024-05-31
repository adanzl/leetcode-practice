"""
 * 给你一个下标从 0 开始的二维整数矩阵 grid，大小为 n * n ，其中的值在 [1, n2] 范围内。
 * 除了 a 出现 两次，b 缺失 之外，每个整数都 恰好出现一次 。
 * 任务是找出重复的数字a 和缺失的数字 b 。
 * 返回一个下标从 0 开始、长度为 2 的整数数组 ans ，其中 ans[0] 等于 a ，ans[1] 等于 b 。
 * 提示：
 * 1、2 <= n == grid.length == grid[i].length <= 50
 * 2、1 <= grid[i][j] <= n * n
 * 3、对于所有满足1 <= x <= n * n 的 x ，恰好存在一个 x 与矩阵中的任何成员都不相等。
 * 4、对于所有满足1 <= x <= n * n 的 x ，恰好存在一个 x 与矩阵中的两个成员相等。
 * 5、除上述的两个之外，对于所有满足1 <= x <= n * n 的 x ，都恰好存在一对 i, j 满足 0 <= i, j <= n - 1 且 grid[i][j] == x 。
 * 链接：https://leetcode.cn/problems/find-missing-and-repeated-values/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=2965 lang=python3
#
# [2965] 找出缺失和重复的数字
#


# @lc code=start
class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = Counter()
        ans = [0, 0]
        n = len(grid)
        s = set([i * n + j + 1 for i in range(n) for j in range(n)])
        for i in range(n):
            for j in range(n):
                if grid[i][j] in cnt:
                    ans[0] = grid[i][j]
                cnt[grid[i][j]] += 1
                s.discard(grid[i][j])
        ans[1] = list(s)[0]
        return ans


# @lc code=end

if __name__ == '__main__':
    # [2,4]
    print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]))
    # [9,5]
    print(Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
