"""
 * 给你一个下标从 0 开始、长度为 n 的二进制字符串 s ，你可以对其执行两种操作：
 * 1、选中一个下标 i 并且反转从下标 0 到下标 i（包括下标 0 和下标 i ）的所有字符，成本为 i + 1 。
 * 2、选中一个下标 i 并且反转从下标 i 到下标 n - 1（包括下标 i 和下标 n - 1 ）的所有字符，成本为 n - i 。
 * 返回使字符串内所有字符 相等 需要的 最小成本 。
 * 反转 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。
 * 提示：
 * 1、1 <= s.length == n <= 10^5
 * 2、s[i] 为 '0' 或 '1'
 * 链接：https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal/
"""


class Solution:

    def minimumCost(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        ans1, ans2 = 0, 0
        for i in range(n // 2 - 1):
            if s[i] == s[i + 1]: continue
            ans1 += i + 1
        for i in range(n - 1, n // 2, -1):
            if s[i] == s[i - 1]: continue
            ans2 += n - i
        return ans1 + ans2 + (n // 2 if s[n // 2 - 1] != s[n // 2] else 0)


if __name__ == '__main__':
    # 9
    print(Solution().minimumCost("010101"))
    # 2
    print(Solution().minimumCost("0011"))
