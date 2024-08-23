"""
 * 对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。
 * 例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
 * 给你一个整数 num ，输出它的补数。
 * 提示：1 <= num < 2^31
 * 链接：https://leetcode.cn/problems/number-complement/
"""

from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#


# @lc code=start
class Solution:

    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        return ~num & ((1 << (num.bit_length())) - 1)


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().findComplement(5))
    # 0
    print(Solution().findComplement(1))
