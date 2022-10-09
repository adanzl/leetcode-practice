"""
 * 给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
 * 提示：1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/numbers-with-repeated-digits/
"""

from functools import cache


class Solution:
    # 数位 DP
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        # 第 i 位开始填充数字，返回合法数字个数
        # is_limit 当前位置是否受到num限制，首次调用要True
        # is_num 是否已经是一个数了，区分是否可以前导0
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s): return int(is_num)
            ret = 0
            if not is_num:
                ret += f(i + 1, mask, False, False)
            up = int(s[i]) if is_limit else 9
            for num in range(0 if is_num else 1, up + 1):
                if (mask >> num) & 1 == 0:
                    ret += f(i + 1, mask | (1 << num), num == int(s[i]) and is_limit, True)
            return ret

        return n - f(0, 0, True, False)


if __name__ == '__main__':
    # 10
    print(Solution().numDupDigitsAtMostN(100))
    # 1
    print(Solution().numDupDigitsAtMostN(20))
    # 262
    print(Solution().numDupDigitsAtMostN(1000))
    # 11
    print(Solution().numDupDigitsAtMostN(101))