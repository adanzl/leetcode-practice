"""
 * 给你一个字符串 word 和一个整数 k。
 * 如果 |freq(word[i]) - freq(word[j])| <= k 对于字符串中所有下标 i 和 j  都成立，则认为 word 是 k 特殊字符串。
 * 此处，freq(x) 表示字符 x 在 word 中的出现频率，而 |y| 表示 y 的绝对值。
 * 返回使 word 成为 k 特殊字符串 需要删除的字符的最小数量。
 * 提示：
 * 1、1 <= word.length <= 10^5
 * 2、0 <= k <= 10^5
 * 3、word 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/
"""
import bisect
from typing import Counter


class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        arr = sorted([c for v, c in Counter(word).items()])
        ans = len(word)
        for i, cnt in enumerate(arr):
            idx = bisect.bisect_left(arr, cnt + k + 1)
            cc = len(arr) - idx
            vv = sum(arr[idx:]) + sum(arr[:i])
            if cc:
                vv -= cc * (cnt + k)
            ans = min(ans, vv)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minimumDeletions("dabdcbdcdcd", k=2))
    # 3
    print(Solution().minimumDeletions("aabcaba", k=0))
    # 1
    print(Solution().minimumDeletions("aaabaaa", k=2))
