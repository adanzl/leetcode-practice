"""
 * 给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。
 * 字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。
 * 但是拆分出来的每个子字符串都必须是 唯一的 。
 * 注意：子字符串 是字符串中的一个连续字符序列。
 * 提示：
 * 1、1 <= s.length <= 16
 * 2、s 仅包含小写英文字母
 * 链接：https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings
"""

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1593 lang=python3
# @lcpr version=20002
#
# [1593] 拆分字符串使唯一子字符串的数目最大
#


# @lc code=start
class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        ans = 1
        st = set()

        def dfs(ii):
            nonlocal ans
            if ii == len(s):
                ans = max(ans, len(st))
                return
            for jj in range(ii, len(s)):
                if s[ii:jj + 1] not in st:
                    st.add(s[ii:jj + 1])
                    dfs(jj + 1)
                    st.remove(s[ii:jj + 1])

        dfs(0)
        return ans


# @lc code=end

#

if __name__ == '__main__':
    # 5
    print(Solution().maxUniqueSplit('ababccc'))
    # 2
    print(Solution().maxUniqueSplit('aba'))
    # 1
    print(Solution().maxUniqueSplit('aa'))
