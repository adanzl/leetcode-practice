"""
 * 给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ：
 * 1、翻转 n 的二进制表示中最右侧位（第 0 位）。
 * 2、如果第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。
 * 返回将 n 转换为 0 的最小操作次数。
 * 提示：0 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-one-bit-operations-to-make-integers-zero/
"""


class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n:
            ans ^= n
            n //= 2
        return ans


if __name__ == '__main__':
    # 12
    print(Solution().minimumOneBitOperations(10))
    # 4
    print(Solution().minimumOneBitOperations(6))
    # 31
    print(Solution().minimumOneBitOperations(16))
    # 756249599
    print(Solution().minimumOneBitOperations(10**9))