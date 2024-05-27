"""
 * 给你一个字符串 s 。s[i] 要么是小写英文字母，要么是问号 '?' 。
 * 对于长度为 m 且 只 含有小写英文字母的字符串 t ，
 * 我们定义函数 cost(i) 为下标 i 之前（也就是范围 [0, i - 1] 中）出现过与 t[i] 相同 字符出现的次数。
 * 字符串 t 的 分数 为所有下标 i 的 cost(i) 之 和 。
 * 比方说，字符串 t = "aab" ：
 * 1、cost(0) = 0
 * 2、cost(1) = 1
 * 3、cost(2) = 0
 * 4、所以，字符串 "aab" 的分数为 0 + 1 + 0 = 1 。
 * 你的任务是用小写英文字母 替换 s 中 所有 问号，使 s 的 分数最小 。
 * 请你返回替换所有问号 '?' 之后且分数最小的字符串。如果有多个字符串的 分数最小 ，那么返回字典序最小的一个。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 要么是小写英文字母，要么是 '?' 。
 * 链接：https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/
"""
from heapq import heapify, heappop, heappush
from typing import Counter


class Solution:

    def minimizeStringValue(self, s: str) -> str:
        cnt = Counter(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            cnt[c] += 0
        del cnt['?']
        h = [[v, k] for k, v in cnt.items()]
        heapify(h)
        ans = list(s)
        ids, chs = [], []
        for i, c in enumerate(s):
            if c == '?':
                cc, ch = heappop(h)
                ids.append(i)
                chs.append(ch)
                heappush(h, [cc + 1, ch])
        for i, c in zip(ids, sorted(chs)):
            ans[i] = c
        return ''.join(ans)


if __name__ == '__main__':
    # "abcdefghijklmnopqrstuvwxyaz"
    print(Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
    # "abc"
    print(Solution().minimizeStringValue("???"))
    # "abac"
    print(Solution().minimizeStringValue("a?a?"))
