"""
 * 给你一个正整数 p 。
 * 你有一个下标从 1 开始的数组 nums ，这个数组包含范围 [1, 2^p - 1] 内所有整数的二进制形式（两端都 包含）。
 * 你可以进行以下操作 任意 次：
 * 1、从 nums 中选择两个元素 x 和 y  。
 * 2、选择 x 中的一位与 y 对应位置的位交换。对应位置指的是两个整数 相同位置 的二进制位。
 * 比方说，如果 x = 1101 且 y = 0011 ，交换右边数起第 2 位后，我们得到 x = 1111 和 y = 0001 。
 * 请你算出进行以上操作 任意次 以后，nums 能得到的 最小非零 乘积。将乘积对 10^9 +  7 取余 后返回。
 * 注意：答案应为取余 之前 的最小值。
 * 提示：1 <= p <= 60
 * 链接：https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements
"""

#
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
#


# @lc code=start
class Solution:

    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        mod = 10**9 + 7
        return pow(2**p - 2, 2**(p - 1) - 1, mod) * (2**p - 1) % mod


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().minNonZeroProduct(1))
    # 6
    print(Solution().minNonZeroProduct(2))
    # 1512
    print(Solution().minNonZeroProduct(3))
    #
    print(Solution().minNonZeroProduct(60))
