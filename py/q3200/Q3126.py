"""
 * 给你一个仅由数字组成的字符串 s，在最多交换一次 相邻 且具有相同 奇偶性 的数字后，返回可以得到的 字典序最小的字符串。
 * 如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。
 * 提示：
 * 1、2 <= s.length <= 100
 * 2、s 仅由数字组成。
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/
"""


class Solution:

    def getSmallestString(self, s: str) -> str:
        n = len(s)
        ans = list(s)
        for i in range(n - 1):
            a, b = int(ans[i]), int(ans[i + 1])
            if a % 2 == b % 2 and b < a:
                ans[i], ans[i + 1] = ans[i + 1], ans[i]
                break
        return ''.join(ans)


if __name__ == '__main__':
    # "43520"
    print(Solution().getSmallestString("45320"))
    # "001"
    print(Solution().getSmallestString("001"))
