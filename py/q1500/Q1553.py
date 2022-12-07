"""
 * 厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：
 * 1、吃掉一个橘子。
 * 2、如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
 * 3、如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
 * 每天你只能从以上 3 种方案中选择一种方案。
 * 请你返回吃掉所有 n 个橘子的最少天数。
 * 提示：1 <= n <= 2*10^9
 * 链接：https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/
"""
from functools import cache


class Solution:

    @cache
    def minDays(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))


if __name__ == '__main__':
    # 4
    print(Solution().minDays(10))
    # 3
    print(Solution().minDays(6))
    # 1
    print(Solution().minDays(1))
    # 6
    print(Solution().minDays(56))
    # 22
    print(Solution().minDays(820592))