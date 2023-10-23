"""
 * 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
 * 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
 * 提示：-2^31 <= n <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/power-of-four/
"""

#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#


# @lc code=start
class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        ln = (n ^ (n - 1)).bit_length() - 1
        return n == 1 << ln and ln & 1 == 0


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isPowerOfFour(16))
    # False
    print(Solution().isPowerOfFour(3))
    # False
    print(Solution().isPowerOfFour(0))
    # False
    print(Solution().isPowerOfFour(8))
    # False
    print(Solution().isPowerOfFour(5))
    # True
    print(Solution().isPowerOfFour(1))