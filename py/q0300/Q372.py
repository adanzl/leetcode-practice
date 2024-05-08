"""
 * 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
 * 提示：
 * 1、1 <= a <= 2^31 - 1
 * 2、1 <= b.length <= 2000
 * 3、0 <= b[i] <= 9
 * 4、b 不含前导 0
 * 链接：https://leetcode.cn/problems/super-pow/
"""

from typing import List

#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方

# @lc code=start


class Solution:

    def superPow(self, a: int, b: List[int]) -> int:
        # x^(a+b) = x^a * x^b
        # x^(a*b) = (x^a)^b
        MOD = 1337
        a %= MOD
        ans = 1
        for e in reversed(b):
            ans = ans * pow(a, e, MOD) % MOD
            a = pow(a, 10, MOD)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 8
    print(Solution().superPow(2, b=[3]))
    # 1024
    print(Solution().superPow(2, b=[1, 0]))
    # 1
    print(Solution().superPow(1, b=[4, 3, 3, 8, 5, 2]))
    # 1198
    print(Solution().superPow(2147483647, b=[2, 0, 0]))
