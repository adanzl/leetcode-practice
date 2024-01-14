"""
 * 给你一个仅由小写英文字母组成的字符串 s 。
 * 如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。
 * 返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。
 * 子字符串 是字符串中的一个连续 非空 字符序列。
 * 提示：
 * 1、3 <= s.length <= 5 * 10^5
 * 2、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/
"""
from collections import defaultdict


class Solution:

    def maximumLength(self, s: str) -> int:
        ch = ' '
        ct = 0
        cnt = defaultdict(list)
        for c in s:
            if c == ch:
                ct += 1
            else:
                cnt[ch].append(ct)
                ct = 1
                ch = c
        cnt[ch].append(ct)

        ans = -1
        n = len(s)
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            fit = False
            for cts in cnt.values():
                v = 0
                for ct in cts:
                    if ct >= mid:
                        v += ct - mid + 1
                if v >= 3:
                    fit = True
                    break
            if fit:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maximumLength("aaaa"))
    # -1
    print(Solution().maximumLength("abcdef"))
    # 1
    print(Solution().maximumLength("abcaba"))
