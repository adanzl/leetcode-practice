"""
 * 给你一个整数 n ，请你将 1 到 n 的二进制表示连接起来，并返回连接结果对应的 十进制 数字对 10^9 + 7 取余的结果。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/
"""
from typing import *


class Solution:

    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans, size, l = 0, 0, 1
        for num in range(1, n + 1):
            if num == l:
                size += 1
                l <<= 1
            ans = ((ans << size) + num) % MOD
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().concatenatedBinary(1))
    # 27
    print(Solution().concatenatedBinary(3))
    # 505379714
    print(Solution().concatenatedBinary(12))