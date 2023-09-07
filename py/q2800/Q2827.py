"""
 * 给你正整数 low ，high 和 k 。
 * 如果一个数满足以下两个条件，那么它是 美丽的 ：
 * 1、偶数数位的数目与奇数数位的数目相同。
 * 2、这个整数可以被 k 整除。
 * 请你返回范围 [low, high] 中美丽整数的数目。
 * 提示：
 * 1、0 < low <= high <= 10^9
 * 2、0 < k <= 20
 * 链接：https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
"""

from functools import cache


class Solution:

    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        def calc(high: int) -> int:
            s = str(high)
            # 数位dp
            # val 的部分把除法的计算量降下来，时间复杂度10**9
            @cache
            def f(idx, is_limit, is_num, balance, val):
                if idx == len(s):
                    return 1 if (balance == 0 and val == 0 and is_num) else 0
                ret = 0
                if not is_num:
                    ret += f(idx + 1, False, False, balance, val)
                down = 0 if is_num else 1
                up = int(s[idx]) if is_limit else 9
                for v in range(down, up + 1):
                    limit = is_limit and v == up
                    n_b = (balance + (1 if v % 2 else -1))
                    ret += f(idx + 1, limit, True, n_b, (val * 10 + v) % k)
                return ret

            return f(0, True, False, 0, 0)

        return calc(high) - calc(low - 1)

    def numberOfBeautifulIntegers1(self, low: int, high: int, k: int) -> int:

        def calc(high: int) -> int:
            s = str(high)
            # 数位dp
            @cache  # 记忆化搜索
            def dfs(i: int, val: int, balance: int, is_limit: bool, is_num: bool) -> int:
                if i == len(s):
                    return int(is_num and val == 0 and balance == 0)  # 找到了一个合法数字
                res = 0
                if not is_num:  # 可以跳过当前数位
                    res = dfs(i + 1, val, balance, False, False)
                d0 = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 high 的一样，那么这一位至多填 s[i]（否则就超过 high 啦）
                for d in range(d0, up + 1):  # 枚举要填入的数字 d
                    res += dfs(i + 1, (val * 10 + d) % k, balance + d % 2 * 2 - 1, is_limit and d == up, True)
                return res

            return dfs(0, 0, 0, True, False)

        return calc(high) - calc(low - 1)


if __name__ == '__main__':
    #
    print(Solution().numberOfBeautifulIntegers(1, 10**9, 1))
    # 1
    print(Solution().numberOfBeautifulIntegers(83, 100, 10))
    # 1
    print(Solution().numberOfBeautifulIntegers(1, high=10, k=1))
    # 2
    print(Solution().numberOfBeautifulIntegers(10, high=20, k=3))
    # 0
    print(Solution().numberOfBeautifulIntegers(5, high=5, k=2))
