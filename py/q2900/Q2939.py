"""
 * 给你三个整数 a ，b 和 n ，请你返回 (a XOR x) * (b XOR x) 的 最大值 且 x 需要满足 0 <= x < 2^n。
 * 由于答案可能会很大，返回它对 10^9 + 7 取余 后的结果。
 * 注意，XOR 是按位异或操作。
 * 提示：
 * 1、0 <= a, b < 250
 * 2、0 <= n <= 50
 * 链接：https://leetcode.cn/problems/maximum-xor-product/
"""


class Solution:

    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        ans_a, ans_b = a, b
        ff = -1
        for i in range(max(a.bit_length(), b.bit_length()) - 1, n - 1, -1):
            fa, fb = a & (1 << i), b & (1 << i)
            if bool(fa) == bool(fb): continue
            ff = 1 if fa else 0
            break

        for i in range(n - 1, -1, -1):
            fa, fb = a & (1 << i), b & (1 << i)
            if bool(fa) == bool(fb):
                ans_a |= 1 << i
                ans_b |= 1 << i
            else:
                if ff == 0 or ff == -1:
                    ans_a |= 1 << i
                    ans_b &= ~(1 << i)
                    if ff == -1:
                        ff = 1
                else:
                    ans_b |= 1 << i
                    ans_a &= ~(1 << i)
        return ans_a * ans_b % (10**9 + 7)


if __name__ == '__main__':
    # 12
    print(Solution().maximumXorProduct(1, b=6, n=3))
    # 12
    print(Solution().maximumXorProduct(0, 7, 2))
    # 2
    print(Solution().maximumXorProduct(0, 3, 1))
    # 98
    print(Solution().maximumXorProduct(12, b=5, n=4))
    # 930
    print(Solution().maximumXorProduct(6, b=7, n=5))
