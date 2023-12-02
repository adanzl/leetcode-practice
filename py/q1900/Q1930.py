"""
 * 给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。
 * 即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
 * 回文 是正着读和反着读一样的字符串。
 * 子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
 * 例如，"ace" 是 "abcde" 的一个子序列。
 * 提示：
 * 1、3 <= s.length <= 10^5
 * 2、s 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/unique-length-3-palindromic-subsequences
"""

#
# @lc app=leetcode.cn id=1930 lang=python3
#
# [1930] 长度为 3 的不同回文子序列
#

# @lc code=start


class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        st = set()
        for c in s:
            if c in d:
                for cc in 'abcdefghijklmnopqrstuvwxyz':
                    if cc in d[c]:
                        st.add(c + cc + c)
            for c0 in d:
                d[c0].add(c)
            if c not in d:
                d[c] = set()
        return len(st)


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().countPalindromicSubsequence("aabca"))
    # 0
    print(Solution().countPalindromicSubsequence("adc"))
    # 4
    print(Solution().countPalindromicSubsequence("bbcbaba"))
