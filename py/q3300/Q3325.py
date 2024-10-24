"""
 * 给你一个字符串 s 和一个整数 k，在 s 的所有子字符串中，请你统计并返回 至少有一个 字符 至少出现 k 次的子字符串总数。
 * 子字符串 是字符串中的一个连续、 非空 的字符序列。
 * 提示：
 * 1、1 <= s.length <= 3000
 * 2、1 <= k <= s.length
 * 3、s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/
"""
from collections import defaultdict

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
            if len(idx[c]) > k:
                idx[c].pop(0)
            ii = -1
            for l in idx.values():
                if len(l) >= k:
                    ii = max(ii, l[0])
            ans += ii + 1
            
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().numberOfSubstrings("abacb", k=2))
    # 15
    print(Solution().numberOfSubstrings("abcde", k=1))
