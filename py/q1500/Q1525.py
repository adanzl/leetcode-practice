"""
 * 给你一个字符串 s ，一个分割被称为 「好分割」 当它满足：将 s 分割成 2 个字符串 p 和 q ，它们连接起来等于 s 且 p 和 q 中不同字符的数目相同。
 * 请你返回 s 中好分割的数目。
 * 提示：
 * 1、s 只包含小写英文字母。
 * 2、1 <= s.length <= 10^5
 * 链接：https://leetcode.cn/problems/number-of-good-ways-to-split-a-string/
"""


class Solution:

    def numSplits(self, s: str) -> int:
        ans = 0
        n = len(s)
        suf_mark = [0] * (n + 1)
        pre_m = 0
        for i in range(n - 1, -1, -1):
            suf_mark[i] = suf_mark[i + 1] | 1 << (ord(s[i]) - ord('a'))
        for i in range(n):
            if pre_m.bit_count() == suf_mark[i].bit_count():
                ans += 1
            pre_m |= 1 << (ord(s[i]) - ord('a'))
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().numSplits("aacaba"))
    # 1
    print(Solution().numSplits("abcd"))
    # 4
    print(Solution().numSplits("aaaaa"))
    # 2
    print(Solution().numSplits("acbadbaada"))