"""
 * 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
 * 「超赞子字符串」需满足满足下述两个条件：
 * 1、该字符串是 s 的一个非空子字符串
 * 2、进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 仅由数字组成
 * 链接：https://leetcode.cn/problems/find-longest-awesome-substring/
"""

#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] 找出最长的超赞子字符串
#


# @lc code=start
class Solution:

    def longestAwesome(self, s: str) -> int:
        p_sum = {0: -1}
        lst = 0
        ans = 0
        for i, c in enumerate(s):
            lst ^= (1 << (int(c) + 1))
            if lst in p_sum:
                ans = max(ans, i - p_sum[lst])
            else:
                p_sum[lst] = i
            for vv in range(1, 11):
                k = lst ^ (1 << vv)
                if k in p_sum:
                    ans = max(ans, i - p_sum[k])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().longestAwesome("00"))
    # 5
    print(Solution().longestAwesome("3242415"))
    # 1
    print(Solution().longestAwesome("12345678"))
    # 6
    print(Solution().longestAwesome("213123"))
