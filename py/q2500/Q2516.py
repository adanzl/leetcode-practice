"""
 * 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
 * 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅由字母 'a'、'b'、'c' 组成
 * 3、0 <= k <= s.length
 * 链接：https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
"""


class Solution:

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        ca, cb, cc = 0, 0, 0
        n = len(s)
        l_cnt_a, l_cnt_b, l_cnt_c = {0: -1}, {0: -1}, {0: -1}
        for i in range(n):
            if s[i] == 'a':
                ca += 1
                l_cnt_a[ca] = i
            if s[i] == 'b':
                cb += 1
                l_cnt_b[cb] = i
            if s[i] == 'c':
                cc += 1
                l_cnt_c[cc] = i
        if ca < k or cb < k or cc < k: return -1
        rca, rcb, rcc = 0, 0, 0
        ans = max(l_cnt_a.get(k, n), l_cnt_b.get(k, n), l_cnt_c.get(k, n)) + 1
        for i in range(n):
            if s[n - 1 - i] == 'a':
                rca += 1
            if s[n - 1 - i] == 'b':
                rcb += 1
            if s[n - 1 - i] == 'c':
                rcc += 1
            ans = min(ans, max(l_cnt_a.get(max(k - rca, 0), n), l_cnt_b.get(max(k - rcb, 0), n), l_cnt_c.get(max(k - rcc, 0), n)) + i + 2)
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().takeCharacters("caaababcaa", 2))
    # 8
    print(Solution().takeCharacters("aabaaaacaabc", 2))
    # -1
    print(Solution().takeCharacters("a", 1))
