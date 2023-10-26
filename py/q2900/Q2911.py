"""
 * 给你一个字符串 s 和一个整数 k ，请你将 s 分成 k 个 子字符串 ，使得每个 子字符串 变成 半回文串 需要修改的字符数目最少。
 * 请你返回一个整数，表示需要修改的 最少 字符数目。
 * 注意：
 * 1、如果一个字符串从左往右和从右往左读是一样的，那么它是一个 回文串 。
 * 2、如果长度为 len 的字符串存在一个满足 1 <= d < len 的正整数 d ，
 *      len % d == 0 成立且所有对 d 做除法余数相同的下标对应的字符连起来得到的字符串都是 回文串 ，
 *      那么我们说这个字符串是 半回文串 。比方说 "aa" ，"aba" ，"adbgad" 和 "abab" 都是 半回文串 ，而 "a" ，"ab" 和 "abca" 不是。
 * 3、子字符串 指的是一个字符串中一段连续的字符序列。
 * 提示：
 * 1、2 <= s.length <= 200
 * 2、1 <= k <= s.length / 2
 * 3、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-changes-to-make-k-semi-palindromes/
"""


class Solution:

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i][j]表示s[i:j+1]修改为半回文修改次数
        dp_hp = [[n] * n for __ in range(n)]

        def calc_p(l, r, d):
            ret = 0
            for idx in range(d):
                ss = s[l + idx:r + 1:d]
                for i in range(len(ss) // 2):
                    if ss[i] != ss[len(ss) - 1 - i]: ret += 1
            return ret

        for i in range(n):
            dp_hp[i][i] = n
            for j in range(i + 1, n):
                vv = n
                ln = j - i + 1
                for d in range(1, ln):
                    if ln % d: continue
                    vv = min(vv, calc_p(i, j, d))
                dp_hp[i][j] = min(dp_hp[i][j], vv)
        # dp[i][j] 表示 前i字符构成的字符串分j份，修改最少
        dp = [[n] * (k + 1) for _ in range(n + 1)]
        for i in range(k + 1):
            dp[0][i] = 0
        for i in range(n):
            dp[i + 1][1] = dp_hp[0][i]
        for i in range(1, k):  # 分组 0 开始
            for j in range(n):  # 字符串索引
                for l in range(j, (i) * 2 - 1, -1):  #
                    dp[j + 1][i + 1] = min(dp[j + 1][i + 1], dp[l][i] + dp_hp[l][j])
                    # print(j, i, dp[j + 1][i + 1], dp[l][i], dp_hp[l][j], l)
        return dp[-1][-1]


if __name__ == '__main__':
    # 3
    print(Solution().minimumChanges("cbacccbabcaa", 1))
    # 3
    print(Solution().minimumChanges("dpqldq", 3))
    # 2
    print(Solution().minimumChanges("abcdef", k=2))
    # 1
    print(Solution().minimumChanges("abcac", k=2))
    # 0
    print(Solution().minimumChanges("aabbaa", k=3))
    # 2
    print(Solution().minimumChanges("acba", 2))
    # 2
    print(Solution().minimumChanges("abcc", 1))
    # 1
    print(Solution().minimumChanges("aq", 1))
