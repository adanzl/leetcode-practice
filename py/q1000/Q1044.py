"""
 * 给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
 * 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
 * 提示：
 * 1、2 <= s.length <= 3 * 10^4
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/longest-duplicate-substring
"""

#
# @lc app=leetcode.cn id=1044 lang=python3
#


# @lc code=start
class Solution:

    def longestDupSubstring(self, s: str) -> str:
        n, BASE = len(s), 26
        cov = lambda x: ord(x) - ord('a')
        ans = ''

        def check(ln):
            nonlocal ans
            base = 0
            for i in range(ln):
                base = base * BASE + cov(s[i])
            vis = set([base])
            r = pow(BASE, ln - 1)
            for i in range(1, n - ln + 1):
                base = (base - r * cov(s[i - 1])) * BASE + cov(s[i + ln - 1])
                if base in vis:
                    ans = s[i:i + ln]
                    return True
                vis.add(base)
            return False

        l, r = 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return ans

    def longestDupSubstring1(self, s: str) -> str:
        n = len(s)
        P = 5
        hs, p = [0] * (n + 5), [1] * (n + 5)
        for i, c in enumerate(s):
            hs[i + 1] = (hs[i] << P) + ord(c) - ord('a') + 1
            p[i + 1] = p[i] << P

        def check(ln):
            st = set([hs[ln]])
            for i in range(ln, n):
                vv = hs[i + 1] & (p[ln] - 1)
                if vv in st:
                    return True, i
                st.add(vv)
            return False, -1

        ans_len, ans_i = 0, -1
        l, r = 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            valid, idx = check(mid)
            if valid:
                ans_i = idx
                ans_len = mid
                l = mid + 1
            else:
                r = mid - 1
        return '' if ans_len == 0 else s[ans_i - ans_len + 1:ans_i + 1]

    def longestDupSubstring2(self, s: str) -> str:
        # 后缀数组
        return ''


# @lc code=end

if __name__ == '__main__':
    # "ma"
    print(Solution().longestDupSubstring('nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy'))
    # "ana"
    print(Solution().longestDupSubstring("banana"))
    # ""
    print(Solution().longestDupSubstring("abcd"))