"""
 * 给你两个正整数 n 和 k。
 * 你可以选择 n 的 二进制表示 中任意一个值为 1 的位，并将其改为 0。
 * 返回使得 n 等于 k 所需要的更改次数。如果无法实现，返回 -1。
 * 提示：1 <= n, k <= 10^6
 * 链接：https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/
"""


class Solution:

    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for i in range(30):
            if (1 << i) & n == 0 and (1 << i) & k != 0:
                return -1
            if (1 << i) & n != 0 and (1 << i) & k == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minChanges(13, k=4))
    # 0
    print(Solution().minChanges(21, k=21))
    # -1
    print(Solution().minChanges(14, k=13))
