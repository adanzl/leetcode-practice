"""
 * 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
 * 如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
 * 提示：1 <= a, b <= 1000
 * 链接：https://leetcode.cn/problems/number-of-common-factors/
"""


class Solution:

    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, max(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().commonFactors(12, 6))
    # 2
    print(Solution().commonFactors(25, 630))