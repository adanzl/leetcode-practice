"""
 * 给你一个字符串 s 。
 * 你需要对 s 执行以下操作 任意 次：
 * 1、选择一个下标 i ，满足 s[i] 左边和右边都 至少 有一个字符与它相同。
 * 2、删除 s[i] 左边 离它 最近 且相同的字符。
 * 3、删除 s[i] 右边 离它 最近 且相同的字符。
 * 请你返回执行完所有操作后， s 的 最短 长度。
 * 提示：
 * 1、1 <= s.length <= 2 * 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-length-of-string-after-operations/
"""
from collections import Counter


class Solution:

    def minimumLength(self, s: str) -> int:
        ans, cnt = len(s), Counter(s)
        for c in cnt.values():
            ans -= (c - 1) // 2 * 2
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().minimumLength("abaacbcbb"))
    # 2
    print(Solution().minimumLength("aa"))
