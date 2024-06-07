"""
 * 给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该 子字符串 的 最大 长度。
 * 提示：
 * 1、2 <= s.length <= 100
 * 2、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/
"""
from typing import Counter


class Solution:

    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cnt = Counter()
            j = i
            while j < len(s) :
                cnt[s[j]] += 1
                if cnt and cnt.most_common()[0][1] > 2:
                    break
                j += 1
            ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maximumLengthSubstring("bcbbbcba"))
    # 2
    print(Solution().maximumLengthSubstring("aaaa"))
