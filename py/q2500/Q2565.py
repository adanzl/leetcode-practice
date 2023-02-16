"""
 * 给你两个字符串 s 和 t 。
 * 你可以从字符串 t 中删除任意数目的字符。
 * 如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：
 * 1、令 left 为删除字符中的最小下标。
 * 2、令 right 为删除字符中的最大下标。
 * 字符串的得分为 right - left + 1 。
 * 请你返回使 t 成为 s 子序列的最小得分。
 * 一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。
 * 提示：
 * 1、1 <= s.length, t.length <= 10^5
 * 2、s 和 t 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/subsequence-with-the-minimum-score/
"""


class Solution:

    def minimumScore(self, s: str, t: str) -> int:
        ans = n = len(t)
        l_idx, r_idx = [-1] * n, [-1] * n
        i_s = 0
        for i, c in enumerate(t):
            while i_s < len(s) and s[i_s] != c:
                i_s += 1
            if i_s < len(s):
                l_idx[i] = i_s
                i_s += 1
        i_s = len(s) - 1
        for i in range(n - 1, -1, -1):
            while i_s >= 0 and s[i_s] != t[i]:
                i_s -= 1
            if i_s >= 0:
                r_idx[i] = i_s
                i_s -= 1

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2  # 个数
            find = False
            if r_idx[mid] != -1:  # 全部删除左边
                find = True
            for i in range(n - mid - 1):
                if l_idx[i] != -1 and r_idx[i + mid + 1] != -1 and l_idx[i] < r_idx[i + mid + 1]:
                    find = True
                    break
            if l_idx[n - mid - 1] != -1:  # 全部删除右边
                find = True
            if find:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minimumScore("abacaba", t="bzaa"))
    # 4
    print(Solution().minimumScore("abacaba", t="bzaaz"))
    # 3
    print(Solution().minimumScore("cde", t="xyz"))
