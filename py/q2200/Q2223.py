"""
 * 你需要从空字符串开始 构造 一个长度为 n 的字符串 s ，构造的过程为每次给当前字符串 前面 添加 一个 字符。
 * 构造过程中得到的所有字符串编号为 1 到 n ，其中长度为 i 的字符串编号为 si 。
 * 比方说，s = "abaca" ，s1 == "a" ，s2 == "ca" ，s3 == "aca" 依次类推。
 * si 的 得分 为 si 和 sn 的 最长公共前缀 的长度（注意 s == sn ）。
 * 给你最终的字符串 s ，请你返回每一个 si 的 得分之和 。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/sum-of-scores-of-built-strings/
"""

#
# @lc app=leetcode.cn id=2223 lang=python3
#
# [2223] 构造字符串的总得分和
#


# @lc code=start
class Solution:

    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n  # 扩展kmp
        ans, l, r = n, 0, 0
        for i in range(1, n):
            # 注：不用 min max，拆开用 < > 比较会更快（仅限于 Python）
            z[i] = max(min(z[i - l], r - i + 1), 0)  
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
            ans += z[i]
        return ans


# @lc code=end

if __name__ == '__main__':
    # 9
    print(Solution().sumScores("babab"))
    # 14
    print(Solution().sumScores("azbazbzaz"))