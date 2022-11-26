"""
 * 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。
 * 你需要切披萨 k-1 次，得到 k 块披萨并送给别人。
 * 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。
 * 如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。
 * 在切完最后一刀后，需要把剩下来的一块送给最后一个人。
 * 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。
 * 提示：
 * 1、1 <= rows, cols <= 50
 * 2、rows == pizza.length
 * 3、cols == pizza[i].length
 * 4、1 <= k <= 10
 * 5、pizza 只包含字符 'A' 和 '.' 。
 * 链接：https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/
"""
from functools import cache
from typing import List


class Solution:

    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        a = [[0] * (cols + 1) for i in range(rows + 1)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                a[i][j] = a[i + 1][j] + a[i][j + 1] - a[i + 1][j + 1] + (1 if pizza[i][j] == 'A' else 0)

        @cache
        def f(x, y, k):
            if a[x][y] == 0: return 0
            if k == 1: return 1
            ans = 0
            # 横着切
            for i in range(x + 1, rows):
                if a[x][y] - a[i][y] == 0: continue  # no apple
                ans += f(i, y, k - 1)
            # 竖着切
            for i in range(y + 1, cols):
                if a[x][y] - a[x][i] == 0: continue
                ans += f(x, i, k - 1)
            return ans % MOD

        return f(0, 0, k)


if __name__ == '__main__':
    # 3
    print(Solution().ways(["A..", "AAA", "..."], 3))
    # 1
    print(Solution().ways(["A..", "AA.", "..."], 3))
    # 1
    print(Solution().ways(["A..", "A..", "..."], 1))
