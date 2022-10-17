"""
 * 给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。例如，如果 digits = ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。
 * 返回 可以生成的小于或等于给定整数 n 的正整数的个数 。
 * 提示：
 * 1、1 <= digits.length <= 9
 * 2、digits[i].length == 1
 * 3、digits[i] 是从 '1' 到 '9' 的数
 * 4、digits 中的所有值都 不同 
 * 5、digits 按 非递减顺序 排列
 * 6、1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/
"""
from typing import List
from functools import cache


class Solution:

    def atMostNGivenDigitSet1(self, digits: List[str], n: int) -> int:
        s = str(n)
        l = len(digits)
        NUMS = [1] + [l**(i + 1) for i in range(len(s))]

        @cache
        def func(idx):
            ret = 0
            if idx == len(s):
                return 1
            num = s[idx]
            for i in digits:
                if i > num:
                    break
                elif i == num:
                    ret += func(idx + 1)
                    break
                else:
                    ret += NUMS[len(s) - 1 - idx]
                    pass
            return ret

        return sum(NUMS[1:-1]) + func(0)

    # 数位DP变种
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        @cache
        def f(idx, is_limit, is_num):
            if idx == len(s): return is_num
            ret = 0 if is_num else f(idx + 1, False, False)
            for d in digits:
                if is_limit and d > s[idx]: break
                ret += f(idx + 1, d == s[idx] and is_limit, True)
            return ret

        return f(0, True, False)


if __name__ == '__main__':
    # 79
    print(Solution().atMostNGivenDigitSet(["1", "2", "3", "6", "7", "8"], 211))
    # 1
    print(Solution().atMostNGivenDigitSet(["3", "5"], 4))
    # 1
    print(Solution().atMostNGivenDigitSet(["7"], 8))
    # 20
    print(Solution().atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
    # 29523
    print(Solution().atMostNGivenDigitSet(["1", "4", "9"], 1000000000))
