"""
 * 给你一个二进制字符串 s。
 * 请你统计并返回其中 1 显著 的 子字符串 的数量。
 * 如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 
 * 提示：
 * 1、1 <= s.length <= 4 * 10^4
 * 2、s 仅包含字符 '0' 和 '1'。。
 * 链接：https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/
"""


class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        idx_0 = [i for i, c in enumerate(s) if c == '0']
        total_1 = n - len(idx_0)
        idx_0.append(n)
        ii = 0
        for l, c in enumerate(s):
            if c == '1':
                ans += idx_0[ii] - l
            for k in range(ii, len(idx_0) - 1):
                cnt0 = k - ii + 1
                if cnt0 * cnt0 > total_1:
                    break
                cnt1 = idx_0[k] - l - (k - ii)
                ans += max(idx_0[k + 1] - idx_0[k] - max(cnt0 * cnt0 - cnt1, 0), 0)
            if c == '0':
                ii += 1

        return ans


if __name__ == '__main__':
    # 21
    print(Solution().numberOfSubstrings("000111100"))
    # 16
    print(Solution().numberOfSubstrings("101101"))
    # 5
    print(Solution().numberOfSubstrings("00011"))
