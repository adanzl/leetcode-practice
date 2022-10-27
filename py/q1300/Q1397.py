"""
 * 给你两个长度为 n 的字符串 s1 和 s2 ，以及一个字符串 evil 。请你返回 好字符串 的数目。
 * 好字符串 的定义为：它的长度为 n ，字典序大于等于 s1 ，字典序小于等于 s2 ，且不包含 evil 为子字符串。
 * 由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。
 * 提示：
 * 1、s1.length == n
 * 2、s2.length == n
 * 3、s1 <= s2
 * 4、1 <= n <= 500
 * 5、1 <= evil.length <= 50
 * 6、所有字符串都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-all-good-strings/
"""

from functools import cache


class Solution:

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        n_e = len(evil)
        # kmp 构建next数组
        next = [0] * n_e
        pre_len = 0
        i = 1
        while i < n_e:
            if evil[pre_len] == evil[i]:
                pre_len += 1
                next[i] = pre_len
                i += 1
            else:
                if pre_len:
                    pre_len -= 1
                else:
                    i += 1

        @cache
        def dfs(idx, up_limit, down_limit, e_i):
            if idx == n: return 1
            up = ord(s2[idx]) if up_limit else ord('z')
            down = ord(s1[idx]) if down_limit else ord('a')
            ret = 0
            for ic in range(down, up + 1):
                if e_i == n_e - 1 and evil[e_i] == chr(ic): continue
                if evil[e_i] == chr(ic):
                    n_ei = e_i + 1
                else:
                    # 穷举 ==============================
                    # while n_ei >= 0:
                    #     if evil[:n_ei + 1] == evil[e_i - n_ei:e_i] + chr(ic):
                    #         break
                    #     n_ei -= 1
                    # kmp优化 ============================
                    n_ei = e_i
                    while n_ei and evil[n_ei] != chr(ic):
                        n_ei = next[n_ei - 1]
                    if evil[n_ei] == chr(ic): n_ei += 1
                    # ====================================
                ret += dfs(idx + 1, up_limit and ic == ord(s2[idx]), down_limit and ic == ord(s1[idx]), n_ei)
            return ret % MOD

        return dfs(0, True, True, 0)


if __name__ == '__main__':
    print(Solution().findGoodStrings(8, "pzdanyao", "wgpmtywi", "abacaba"))
    # 500543753
    print(Solution().findGoodStrings(8, "pzdanyao", "wgpmtywi", "sdka"))
    # 51
    print(Solution().findGoodStrings(2, "aa", "da", "b"))
    # 7
    print(Solution().findGoodStrings(2, "pz", "qg", "qa"))
    # 0
    print(Solution().findGoodStrings(8, "leetcode", "leetgoes", "leet"))
    # 2
    print(Solution().findGoodStrings(2, "gx", "gz", "x"))