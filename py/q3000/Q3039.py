"""
 * 给你一个字符串 s 。
 * 请你进行以下操作直到 s 为 空 ：
 * 每次操作 依次 遍历 'a' 到 'z'，如果当前字符出现在 s 中，那么删除出现位置 最早 的该字符。
 * 请你返回进行 最后 一次操作 之前 的字符串 s 。
 * 提示：
 * 1、1 <= s.length <= 5 * 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/apply-operations-to-make-string-empty/description/
"""
from typing import Counter


class Solution:

    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        mc = max(cnt.values())
        ans = []
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if cnt[c] == mc and c not in ans:
                ans.insert(0, c)
        return ''.join(ans)


if __name__ == '__main__':
    # "ba"
    print(Solution().lastNonEmptyString("aabcbbca"))
    # "abcd"
    print(Solution().lastNonEmptyString("abcd"))
