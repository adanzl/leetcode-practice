"""
 * 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：
 * 1、类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
 * 2、类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
 * 请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。
 * 我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。
 * 比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 要么是 '0' ，要么是 '1' 。
 * 链接：https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
"""
from itertools import accumulate


class Solution:

    def minFlips(self, s: str) -> int:
        n = len(s)
        dp0, dp1 = [0] * n, [0] * n
        for i, c in enumerate(s):
            if i & 1:  # odd
                if c == '1': dp1[i] += 1
                else: dp0[i] += 1
            else:
                if c == '1': dp0[i] += 1
                else: dp1[i] += 1
        pre0, pre1 = [0] + list(accumulate(dp0)), [0] + list(accumulate(dp1))
        ans = min(pre0[-1], pre1[-1])
        for i in range(n):
            if n & 1:  # odd: pre0 end with 0, pre1 end with 1
                ans = min(ans, pre0[i] + pre1[-1] - pre1[i])
                ans = min(ans, pre1[i] + pre0[-1] - pre0[i])
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().minFlips("001000000010"))
    # 0
    print(Solution().minFlips("01101"))
    # 5
    print(Solution().minFlips("10001100101000000"))
    # 9
    print(Solution().minFlips("10000110111100110101010010101"))
    # 2
    print(Solution().minFlips("111000"))
    # 0
    print(Solution().minFlips("010"))
    # 1
    print(Solution().minFlips("1110"))