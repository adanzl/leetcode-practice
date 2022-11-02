"""
 * 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/
"""
from typing import Counter


class Solution:

    def smallestSubsequence(self, s: str) -> str:
        cs = Counter(s)
        ss = []
        for c in s:
            cs[c] -= 1
            if c in ss: continue
            while ss and cs[ss[-1]] > 0 and ss[-1] >= c:
                ss.pop()
            ss.append(c)
        return ''.join(ss)


if __name__ == '__main__':
    # "abc"
    print(Solution().smallestSubsequence("bcabc"))
    # "acdb"
    print(Solution().smallestSubsequence("cbacdcbc"))