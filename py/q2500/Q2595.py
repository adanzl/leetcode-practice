"""
 * 给你一个 正 整数 n 。
 * 用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。
 * 用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。
 * 返回整数数组 answer ，其中 answer = [even, odd] 。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/number-of-even-and-odd-bits/
"""
from typing import List


class Solution:

    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1
        return ans


if __name__ == '__main__':
    # [2,0]
    print(Solution().evenOddBit(17))
    # [0,1]
    print(Solution().evenOddBit(2))
    #
    # print(Solution().evenOddBit())