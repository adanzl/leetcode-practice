"""
 * 给你两个整数 n 和 x 。你需要构造一个长度为 n 的 正整数 数组 nums ，对于所有 0 <= i < n - 1 ，
 * 满足 nums[i + 1] 大于 nums[i] ，并且数组 nums 中所有元素的按位 AND 运算结果为 x 。
 * 返回 nums[n - 1] 可能的 最小 值。
 * 提示：1 <= n, x <= 10^8
 * 链接：https://leetcode.cn/problems/minimum-array-end/
"""


class Solution:

    def minEnd(self, n: int, x: int) -> int:
        i_n, ans = 0, x
        n -= 1
        while n:
            b = n & 1
            while (1 << i_n) & x:
                i_n += 1
            ans += b << i_n
            i_n += 1
            n >>= 1
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().minEnd(3, x=4))
    # 15
    print(Solution().minEnd(2, x=7))
