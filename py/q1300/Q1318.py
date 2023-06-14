"""
 * 给你三个正整数 a、b 和 c。
 * 你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。
 * 「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
 * 提示：
 * 1、1 <= a <= 10^9
 * 2、1 <= b <= 10^9
 * 3、1 <= c <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""


class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        ll = max(a.bit_length(), b.bit_length(), c.bit_length())
        ans = 0
        for i in range(ll):
            if (c >> i) & 1 == 1:
                if ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0:
                    ans += 1
            else:
                if ((a >> i) & 1) == 1:
                    ans += 1
                if ((b >> i) & 1) == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minFlips(2, b=6, c=5))
    # 1
    print(Solution().minFlips(4, b=2, c=7))
    # 0
    print(Solution().minFlips(1, b=2, c=3))
