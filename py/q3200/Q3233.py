"""
 * 给你两个 正整数 l 和 r。对于任何数字 x，x 的所有正因数（除了 x 本身）被称为 x 的 真因数。
 * 如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：
 * 1、数字 4 是 特殊数字，因为它的真因数为 1 和 2。
 * 2、数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
 * 返回区间 [l, r] 内 不是 特殊数字 的数字数量。
 * 提示：1 <= l <= r <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/
"""
import bisect

LIMIT = 10**5 + 1
b_prime = [0] * LIMIT
prime_list = []
mn = LIMIT
for i in range(2, LIMIT):
    if not b_prime[i]:
        if prime_list:
            if i - prime_list[-1] < mn:
                mn = i - prime_list[-1]
        prime_list.append(i)

    for prime in prime_list:
        nx = prime * i
        if nx < LIMIT:
            b_prime[nx] = True
        else:
            break


class Solution:

    def nonSpecialCount(self, l: int, r: int) -> int:
        l_idx = bisect.bisect_left(prime_list, l**0.5)
        r_idx = bisect.bisect_right(prime_list, r**0.5)
        ans = (r - l + 1) - (r_idx - l_idx)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().nonSpecialCount(1, 4))
    # 3
    print(Solution().nonSpecialCount(5, r=7))
    # 11
    print(Solution().nonSpecialCount(4, r=16))
