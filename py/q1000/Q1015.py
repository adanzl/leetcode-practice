"""
 * 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
 * 返回 n 的长度。如果不存在这样的 n ，就返回-1。
 * 注意： n 不符合 64 位带符号整数。
 * 提示：1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/smallest-integer-divisible-by-k/
"""


class Solution:

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0: return -1
        if k == 1: return 1
        s = set()
        ans, r = 1, 1
        while r != 0:
            if r in s: return -1
            s.add(r)
            r = (r * 10 + 1) % k
            ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().smallestRepunitDivByK(3))
    # 1
    print(Solution().smallestRepunitDivByK(1))
    # -1
    print(Solution().smallestRepunitDivByK(2))