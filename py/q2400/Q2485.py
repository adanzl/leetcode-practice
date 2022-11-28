"""
 * 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：
 * 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
 * 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/find-the-pivot-integer/
"""
from itertools import accumulate


class Solution:

    def pivotInteger(self, n: int) -> int:
        sm = [0] + list(accumulate(list(range(1, n + 1))))
        for i in range(n):
            if sm[i + 1] == sm[-1] - sm[i]: return i + 1
        return -1


if __name__ == '__main__':
    # 6
    print(Solution().pivotInteger(8))
    # 1
    print(Solution().pivotInteger(1))
    # -1
    print(Solution().pivotInteger(4))