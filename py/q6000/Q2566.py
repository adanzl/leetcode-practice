"""
 * 给你一个整数 num 。你知道 Danny Mittal 会偷偷将 0 到 9 中的一个数字 替换 成另一个数字。
 * 请你返回将 num 中 恰好一个 数字进行替换后，得到的最大值和最小值的差位多少。
 * 注意：
 * 1、当 Danny 将一个数字 d1 替换成另一个数字 d2 时，Danny 需要将 nums 中所有 d1 都替换成 d2 。
 * 2、Danny 可以将一个数字替换成它自己，也就是说 num 可以不变。
 * 3、Danny 可以将数字分别替换成两个不同的数字分别得到最大值和最小值。
 * 4、替换后得到的数字可以包含前导 0 。
 * 5、Danny Mittal 获得周赛 326 前 10 名，让我们恭喜他。
 * 提示：1 <= num <= 10^8
 * 链接：https://leetcode.cn/problems/maximum-difference-by-remapping-a-digit/
"""


class Solution:

    def minMaxDifference(self, num: int) -> int:
        mx, mn = 0, 10**9
        for i in range(10):
            for j in range(10):
                if i == j:
                    continue
                num2 = str(num).replace(str(i), str(j))
                mx, mn = max(mx, int(num2)), min(mn, int(num2))
        return mx - mn


if __name__ == '__main__':
    # 99009
    print(Solution().minMaxDifference(11891))
    # 99
    print(Solution().minMaxDifference(90))