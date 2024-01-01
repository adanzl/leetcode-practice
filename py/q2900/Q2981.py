"""
 * 给你一个仅由小写英文字母组成的字符串 s 。
 * 如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。
 * 返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。
 * 子字符串 是字符串中的一个连续 非空 字符序列。
 * 提示：
 * 1、3 <= s.length <= 50
 * 2、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i/
"""
from typing import Counter


class Solution:

    def maximumLength(self, s: str) -> int:
        ans = -1
        n = len(s)

        def check(ln):
            cnt = Counter()
            for i in range(n):
                j = i + 1
                while j < min(i + ln, n):
                    if s[j] != s[i]:
                        break
                    j += 1
                if j - i >= ln:
                    cnt[s[i]] += 1
            return cnt and cnt.most_common(1)[0][1] >= 3

        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # -1
    print(Solution().maximumLength("abcdef"))
    # 1
    print(Solution().maximumLength("abcaba"))
    # 2
    print(Solution().maximumLength("aaaa"))
